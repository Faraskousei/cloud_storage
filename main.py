from flask import Flask, render_template, request, redirect, url_for, flash, send_file, jsonify, session
from flask_login import LoginManager, current_user, login_required
from werkzeug.utils import secure_filename
from models import db, User, Team, File, init_database
from auth import auth_bp, require_admin, require_team_access
from config import config
import os
import uuid
import mimetypes
from datetime import datetime

def create_app():
    """Create and configure Flask application"""
    app = Flask(__name__)
    
    # Load configuration
    config_name = os.environ.get('FLASK_ENV', 'development')
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    db.init_app(app)
    
    # Initialize LoginManager
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Silakan login untuk mengakses halaman ini.'
    login_manager.login_message_category = 'info'
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    
    # Initialize database
    init_database(app)
    
    return app

app = create_app()

def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def format_file_size(size_bytes):
    """Format file size in human readable format"""
    if size_bytes == 0:
        return "0 B"
    size_names = ["B", "KB", "MB", "GB"]
    i = 0
    while size_bytes >= 1024 and i < len(size_names) - 1:
        size_bytes /= 1024.0
        i += 1
    return f"{size_bytes:.1f} {size_names[i]}"

def get_user_files():
    """Get files for current user's team"""
    if current_user.is_admin:
        # Admin can see all files
        files = File.query.all()
    else:
        # Regular users can only see files from their team
        files = File.query.filter_by(team_id=current_user.team_id).all()
    
    file_list = []
    for file in files:
        file_list.append({
            'id': file.id,
            'name': file.original_name,
            'size': file.file_size,
            'size_formatted': file.format_file_size(),
            'extension': file.get_file_extension(),
            'upload_time': file.created_at,
            'owner': file.owner.full_name,
            'team': file.team.name,
            'team_color': file.team.color
        })
    
    return sorted(file_list, key=lambda x: x['upload_time'], reverse=True)

@app.route('/')
def index():
    """Redirect to dashboard"""
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return redirect(url_for('auth.login'))

@app.route('/dashboard')
@login_required
def dashboard():
    """Dashboard dengan file berdasarkan team"""
    files = get_user_files()
    
    # Statistics
    total_files = len(files)
    total_size = sum(file['size'] for file in files)
    team_files = len([f for f in files if f['team'] == current_user.get_team_name()])
    
    # Get team info
    teams = Team.query.all()
    team_stats = []
    for team in teams:
        team_file_count = File.query.filter_by(team_id=team.id).count()
        team_stats.append({
            'name': team.name,
            'color': team.color,
            'file_count': team_file_count
        })
    
    return render_template('dashboard.html', 
                         files=files, 
                         total_files=total_files,
                         total_size=total_size,
                         team_files=team_files,
                         team_stats=team_stats)

@app.route('/upload', methods=['POST'])
@login_required
def upload_file():
    """Upload file dengan team isolation"""
    if 'file' not in request.files:
        flash('Tidak ada file yang dipilih', 'error')
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        flash('Tidak ada file yang dipilih', 'error')
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        try:
            # Generate unique filename
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            unique_filename = f"{name}_{uuid.uuid4().hex[:8]}{ext}"
            
            # Create team-specific upload directory
            upload_folder = os.path.join(app.config['UPLOAD_FOLDER'], f"team_{current_user.team_id}")
            if not os.path.exists(upload_folder):
                os.makedirs(upload_folder)
            
            file_path = os.path.join(upload_folder, unique_filename)
            file.save(file_path)
            
            # Save file info to database
            new_file = File(
                original_name=filename,
                stored_name=unique_filename,
                file_path=file_path,
                file_size=os.path.getsize(file_path),
                file_type=ext[1:] if ext else 'unknown',
                mime_type=mimetypes.guess_type(file_path)[0],
                owner_id=current_user.id,
                team_id=current_user.team_id
            )
            
            db.session.add(new_file)
            db.session.commit()
            
            flash(f'File "{filename}" berhasil diupload!', 'success')
            
        except Exception as e:
            db.session.rollback()
            flash(f'Error saat upload: {str(e)}', 'error')
    else:
        flash('Tipe file tidak diizinkan', 'error')
    
    return redirect(url_for('dashboard'))

@app.route('/download/<int:file_id>')
@login_required
def download_file(file_id):
    """Download file dengan team access control"""
    file = File.query.get_or_404(file_id)
    
    # Check team access
    if not current_user.is_admin and file.team_id != current_user.team_id:
        flash('Akses ditolak. File tidak dapat diakses.', 'error')
        return redirect(url_for('dashboard'))
    
    if os.path.exists(file.file_path):
        return send_file(file.file_path, as_attachment=True, download_name=file.original_name)
    else:
        flash('File tidak ditemukan', 'error')
        return redirect(url_for('dashboard'))

@app.route('/view/<int:file_id>')
@login_required
def view_file(file_id):
    """Preview file dengan team access control"""
    file = File.query.get_or_404(file_id)
    
    # Check team access
    if not current_user.is_admin and file.team_id != current_user.team_id:
        flash('Akses ditolak. File tidak dapat diakses.', 'error')
        return redirect(url_for('dashboard'))
    
    if os.path.exists(file.file_path):
        mime_type, _ = mimetypes.guess_type(file.file_path)
        if mime_type and mime_type.startswith(('image/', 'text/', 'application/pdf')):
            return send_file(file.file_path)
        else:
            flash('File tidak dapat dipreview', 'error')
            return redirect(url_for('dashboard'))
    else:
        flash('File tidak ditemukan', 'error')
        return redirect(url_for('dashboard'))

@app.route('/delete/<int:file_id>', methods=['POST'])
@login_required
def delete_file(file_id):
    """Delete file dengan team access control"""
    file = File.query.get_or_404(file_id)
    
    # Check team access
    if not current_user.is_admin and file.team_id != current_user.team_id:
        flash('Akses ditolak. File tidak dapat dihapus.', 'error')
        return redirect(url_for('dashboard'))
    
    try:
        # Delete physical file
        if os.path.exists(file.file_path):
            os.remove(file.file_path)
        
        # Delete from database
        db.session.delete(file)
        db.session.commit()
        
        flash(f'File "{file.original_name}" berhasil dihapus', 'success')
        
    except Exception as e:
        db.session.rollback()
        flash(f'Error saat menghapus file: {str(e)}', 'error')
    
    return redirect(url_for('dashboard'))

@app.route('/api/files')
@login_required
def api_files():
    """API endpoint untuk file data"""
    files = get_user_files()
    return jsonify(files)

@app.route('/admin/users')
@login_required
@require_admin
def admin_users():
    """Admin page untuk manage users"""
    users = User.query.all()
    teams = Team.query.all()
    return render_template('admin/users.html', users=users, teams=teams)

@app.route('/admin/teams')
@login_required
@require_admin
def admin_teams():
    """Admin page untuk manage teams"""
    teams = Team.query.all()
    return render_template('admin/teams.html', teams=teams)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
