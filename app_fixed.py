import os
import uuid
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash, send_file, jsonify
from werkzeug.utils import secure_filename
import mimetypes
from flask_login import LoginManager, login_required, current_user, login_user, logout_user
from models import db, User, Team, File, init_database
from config import config

app = Flask(__name__)

# Ambil konfigurasi dari environment variable
config_name = os.environ.get('FLASK_ENV', 'development')
app.config.from_object(config[config_name])

# Initialize database
db.init_app(app)

# Ensure upload folder exists
def ensure_upload_folder():
    """Ensure upload folder exists"""
    upload_folder = app.config['UPLOAD_FOLDER']
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
        print(f"✅ Created upload folder: {upload_folder}")
    else:
        print(f"✅ Upload folder exists: {upload_folder}")

# Create upload folder on startup
with app.app_context():
    ensure_upload_folder()

# Konfigurasi Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Silakan login untuk mengakses halaman ini.'
login_manager.login_message_category = 'info'

# User loader untuk Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Context processor untuk current_user
@app.context_processor
def inject_user():
    return dict(current_user=current_user)

# Error handlers
@app.errorhandler(500)
def internal_error(error):
    """Handle 500 Internal Server Error"""
    return render_template('error.html', 
                         error_code=500, 
                         error_message="Internal Server Error",
                         error_description="Something went wrong on our end. Please try again later."), 500

@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 Not Found Error"""
    return render_template('error.html', 
                         error_code=404, 
                         error_message="Page Not Found",
                         error_description="The page you are looking for does not exist."), 404

@app.errorhandler(403)
def forbidden_error(error):
    """Handle 403 Forbidden Error"""
    return render_template('error.html', 
                         error_code=403, 
                         error_message="Forbidden",
                         error_description="You don't have permission to access this resource."), 403

def allowed_file(filename):
    """Check jika tipe file diizinkan"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def format_file_size(size_bytes):
    """Format ukuran file"""
    if size_bytes == 0:
        return "0 B"
    size_names = ["B", "KB", "MB", "GB"]
    i = 0
    size = float(size_bytes)
    while size >= 1024 and i < len(size_names) - 1:
        size /= 1024.0
        i += 1
    return f"{size:.1f} {size_names[i]}"

@app.route('/')
def index():
    """Halaman utama - menampilkan daftar file"""
    try:
        # Jika belum login, redirect ke halaman login
        if not current_user.is_authenticated:
            return redirect(url_for('login'))
        
        files = get_file_info()
        return render_template('index.html', files=files)
        
    except Exception as e:
        print(f"❌ Index route error: {str(e)}")
        flash(f'Error loading dashboard: {str(e)}', 'error')
        return render_template('error.html', 
                             error_code=500, 
                             error_message="Dashboard Error",
                             error_description="Unable to load dashboard. Please try again later."), 500

def get_file_info():
    """Mengambil informasi file dari database"""
    if current_user.is_authenticated:
        if current_user.is_admin:
            # Admin bisa melihat semua file dari semua tim
            files = File.query.order_by(File.created_at.desc()).all()
            return files
        else:
            # User biasa hanya bisa melihat file dari tim mereka
            files = File.query.filter_by(team_id=current_user.team_id).order_by(File.created_at.desc()).all()
            return files
    return []

@app.route('/upload', methods=['POST'])
@login_required
def upload_file():
    """Upload file baru - hanya untuk user yang sudah login"""
    try:
        if 'file' not in request.files:
            return jsonify({
                'success': False,
                'error': 'Tidak ada file yang dipilih'
            })
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({
                'success': False,
                'error': 'Tidak ada file yang dipilih'
            })
        
        if file and allowed_file(file.filename):
            # Buat nama file yang aman dan unik
            filename = secure_filename(file.filename)
            name, ext = os.path.splitext(filename)
            unique_filename = f"{name}_{uuid.uuid4().hex[:8]}{ext}"
            
            # Simpan file ke folder
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
            file.save(file_path)
            
            # Simpan informasi file ke database
            file_record = File(
                original_name=filename,
                stored_name=unique_filename,
                file_path=file_path,
                file_size=os.path.getsize(file_path),
                file_type=ext[1:].lower() if ext else 'unknown',
                mime_type=mimetypes.guess_type(file_path)[0],
                download_key=File().generate_download_key(),  # Generate unique download key
                owner_id=current_user.id,
                team_id=current_user.team_id
            )
            
            db.session.add(file_record)
            db.session.commit()
            
            # Return file data for AJAX
            return jsonify({
                'success': True,
                'message': f'File "{filename}" berhasil diupload!',
                'file': {
                    'id': file_record.id,
                    'original_name': file_record.original_name,
                    'stored_name': file_record.stored_name,
                    'file_type': file_record.file_type,
                    'file_size_formatted': file_record.format_file_size(),
                    'created_at': file_record.created_at.strftime('%d/%m/%Y'),
                    'team': {
                        'name': file_record.team.name,
                        'color': file_record.team.color
                    } if file_record.team else None
                }
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Tipe file tidak diizinkan. File yang diizinkan: ' + ', '.join(app.config['ALLOWED_EXTENSIONS'])
            })
    
    except Exception as e:
        print(f"❌ Upload error: {str(e)}")
        return jsonify({
            'success': False,
            'error': f'Error saat upload: {str(e)}'
        })

@app.route('/copy-link/<int:file_id>')
@login_required
def copy_link(file_id):
    """Generate copy link untuk file"""
    try:
        if current_user.is_admin:
            # Admin bisa copy link file dari semua tim
            file_record = File.query.get(file_id)
        else:
            # User biasa hanya bisa copy link file dari tim mereka
            file_record = File.query.filter_by(
                id=file_id, 
                team_id=current_user.team_id
            ).first()
        
        if not file_record:
            flash('File tidak ditemukan atau Anda tidak memiliki akses!', 'error')
            return redirect(url_for('index'))
        
        # Generate download dan preview URL
        base_url = request.url_root.rstrip('/')
        download_url = file_record.get_download_url(base_url)
        preview_url = file_record.get_preview_url(base_url)
        
        return jsonify({
            'success': True,
            'download_url': download_url,
            'preview_url': preview_url,
            'file_name': file_record.original_name,
            'file_type': file_record.file_type
        })
        
    except Exception as e:
        print(f"❌ Copy link error: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/download/<download_key>')
def secure_download(download_key):
    """Secure download dengan key - tidak perlu login"""
    try:
        # Cari file berdasarkan download_key
        file_record = File.query.filter_by(download_key=download_key).first()
        
        if not file_record:
            flash('File tidak ditemukan atau link download tidak valid!', 'error')
            return redirect(url_for('login'))
        
        # Cek apakah file ada di filesystem
        if not os.path.exists(file_record.file_path):
            flash('File tidak ditemukan di server!', 'error')
            return redirect(url_for('login'))
        
        # Download file
        return send_file(
            file_record.file_path,
            as_attachment=True,
            download_name=file_record.original_name,
            mimetype=file_record.mime_type
        )
        
    except Exception as e:
        print(f"❌ Secure download error: {str(e)}")
        flash(f'Error saat download: {str(e)}', 'error')
        return redirect(url_for('login'))

@app.route('/preview/<download_key>')
def preview_file(download_key):
    """Preview file dengan key - tidak perlu login"""
    try:
        # Cari file berdasarkan download_key
        file_record = File.query.filter_by(download_key=download_key).first()
        
        if not file_record:
            return render_template('error.html', 
                                 error_code=404, 
                                 error_message="File Not Found",
                                 error_description="File tidak ditemukan atau link tidak valid!"), 404
        
        # Cek apakah file ada di filesystem
        if not os.path.exists(file_record.file_path):
            return render_template('error.html', 
                                 error_code=404, 
                                 error_message="File Not Found",
                                 error_description="File tidak ditemukan di server!"), 404
        
        # Preview file (tidak sebagai attachment)
        return send_file(
            file_record.file_path,
            as_attachment=False,
            mimetype=file_record.mime_type
        )
        
    except Exception as e:
        print(f"❌ Preview error: {str(e)}")
        return render_template('error.html', 
                             error_code=500, 
                             error_message="Preview Error",
                             error_description=f"Error saat preview: {str(e)}"), 500

@app.route('/download_logged_in/<filename>')
@login_required
def download_file(filename):
    """Download file - hanya untuk user yang sudah login"""
    try:
        if current_user.is_admin:
            # Admin bisa download file dari semua tim
            file_record = File.query.filter_by(stored_name=filename).first()
        else:
            # User biasa hanya bisa download file dari tim mereka
            file_record = File.query.filter_by(
                stored_name=filename, 
                team_id=current_user.team_id
            ).first()
        
        if not file_record:
            flash('File tidak ditemukan atau Anda tidak memiliki akses!', 'error')
            return redirect(url_for('index'))
        
        return send_file(
            file_record.file_path,
            as_attachment=True,
            download_name=file_record.original_name,
            mimetype=file_record.mime_type
        )
        
    except Exception as e:
        print(f"❌ Download error: {str(e)}")
        flash(f'Error saat download: {str(e)}', 'error')
        return redirect(url_for('index'))

@app.route('/view/<filename>')
@login_required
def view_file(filename):
    """View file di browser - hanya untuk user yang sudah login"""
    try:
        if current_user.is_admin:
            file_record = File.query.filter_by(stored_name=filename).first()
        else:
            file_record = File.query.filter_by(
                stored_name=filename, 
                team_id=current_user.team_id
            ).first()
        
        if not file_record:
            flash('File tidak ditemukan atau Anda tidak memiliki akses!', 'error')
            return redirect(url_for('index'))
        
        # Untuk file gambar atau teks, tampilkan langsung
        if file_record.file_type in ['png', 'jpg', 'jpeg', 'gif', 'txt']:
            return send_file(file_record.file_path, mimetype=file_record.mime_type)
        else:
            flash('Tipe file tidak dapat ditampilkan langsung. Silakan download.', 'info')
            return redirect(url_for('index'))
            
    except Exception as e:
        print(f"❌ View file error: {str(e)}")
        flash(f'Error saat melihat file: {str(e)}', 'error')
        return redirect(url_for('index'))

@app.route('/pdf_viewer/<filename>')
@login_required
def pdf_viewer(filename):
    """Tampilkan PDF menggunakan PDF.js - hanya untuk user yang sudah login"""
    try:
        if current_user.is_admin:
            file_record = File.query.filter_by(stored_name=filename).first()
        else:
            file_record = File.query.filter_by(
                stored_name=filename, 
                team_id=current_user.team_id
            ).first()
        
        if not file_record or file_record.file_type != 'pdf':
            flash('File PDF tidak ditemukan atau Anda tidak memiliki akses!', 'error')
            return redirect(url_for('index'))
        
        return render_template('pdf_viewer.html', pdf_url=url_for('download_file', filename=filename))
        
    except Exception as e:
        print(f"❌ PDF viewer error: {str(e)}")
        flash(f'Error saat menampilkan PDF: {str(e)}', 'error')
        return redirect(url_for('index'))

@app.route('/delete/<filename>', methods=['POST'])
@login_required
def delete_file(filename):
    """Hapus file - hanya untuk user yang sudah login"""
    try:
        if current_user.is_admin:
            file_record = File.query.filter_by(stored_name=filename).first()
        else:
            file_record = File.query.filter_by(
                stored_name=filename, 
                owner_id=current_user.id, 
                team_id=current_user.team_id
            ).first()
        
        if not file_record:
            flash('File tidak ditemukan atau Anda tidak memiliki akses untuk menghapus!', 'error')
            return redirect(url_for('index'))
        
        # Hapus file dari filesystem
        if os.path.exists(file_record.file_path):
            os.remove(file_record.file_path)
        
        # Hapus dari database
        db.session.delete(file_record)
        db.session.commit()
        
        flash(f'File "{file_record.original_name}" berhasil dihapus!', 'success')
        return redirect(url_for('index'))
        
    except Exception as e:
        print(f"❌ Delete file error: {str(e)}")
        flash(f'Error saat menghapus file: {str(e)}', 'error')
        return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Halaman login"""
    try:
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        
        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            
            user = User.query.filter_by(username=username).first()
            
            if user and user.check_password(password):
                login_user(user)
                user.last_login = datetime.utcnow()
                db.session.commit()
                flash(f'Selamat datang kembali, {user.full_name}!', 'success')
                return redirect(url_for('index'))
            else:
                flash('Username atau password salah!', 'error')
        
        return render_template('login.html')
        
    except Exception as e:
        print(f"❌ Login route error: {str(e)}")
        flash(f'Error loading login page: {str(e)}', 'error')
        return render_template('error.html', 
                             error_code=500, 
                             error_message="Login Page Error",
                             error_description="Unable to load login page. Please try again later."), 500

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Halaman register"""
    try:
        if request.method == 'POST':
            full_name = request.form.get('full_name')
            username = request.form.get('username')
            email = request.form.get('email')
            password = request.form.get('password')
            confirm_password = request.form.get('confirm_password')
            team_id = request.form.get('team_id')
            
            # Validasi form
            if not all([full_name, username, email, password, confirm_password, team_id]):
                flash('Semua field harus diisi!', 'error')
                return render_template('register.html', teams=Team.query.all())
            
            if password != confirm_password:
                flash('Password dan konfirmasi password tidak sama!', 'error')
                return render_template('register.html', teams=Team.query.all())
            
            if len(password) < 6:
                flash('Password minimal 6 karakter!', 'error')
                return render_template('register.html', teams=Team.query.all())
            
            # Cek apakah username sudah ada
            if User.query.filter_by(username=username).first():
                flash('Username sudah digunakan!', 'error')
                return render_template('register.html', teams=Team.query.all())
            
            # Cek apakah email sudah ada
            if User.query.filter_by(email=email).first():
                flash('Email sudah digunakan!', 'error')
                return render_template('register.html', teams=Team.query.all())
            
            # Cek apakah team_id valid
            team = Team.query.get(team_id)
            if not team:
                flash('Tim tidak valid!', 'error')
                return render_template('register.html', teams=Team.query.all())
            
            try:
                # Buat user baru
                new_user = User(
                    full_name=full_name,
                    username=username,
                    email=email,
                    team_id=team_id,
                    is_admin=False,
                    is_active=True
                )
                new_user.set_password(password)
                
                db.session.add(new_user)
                db.session.commit()
                
                flash(f'Akun berhasil dibuat! Selamat datang {full_name}!', 'success')
                return redirect(url_for('login'))
                
            except Exception as e:
                db.session.rollback()
                flash(f'Error saat membuat akun: {str(e)}', 'error')
                return render_template('register.html', teams=Team.query.all())
    
        # Jika sudah login, redirect ke index
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        
        return render_template('register.html', teams=Team.query.all())
        
    except Exception as e:
        print(f"❌ Register route error: {str(e)}")
        flash(f'Error loading register page: {str(e)}', 'error')
        return render_template('error.html', 
                             error_code=500, 
                             error_message="Register Page Error",
                             error_description="Unable to load registration page. Please try again later."), 500

@app.route('/logout')
@login_required
def logout():
    """Logout user"""
    logout_user()
    flash('Anda telah logout.', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    # Inisialisasi database jika belum ada
    with app.app_context():
        db.create_all()
        init_database(app)
    app.run(debug=True)
