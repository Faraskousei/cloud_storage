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
                         error_description="The page you're looking for doesn't exist."), 404

@app.errorhandler(403)
def forbidden_error(error):
    """Handle 403 Forbidden Error"""
    return render_template('error.html', 
                         error_code=403, 
                         error_message="Access Forbidden",
                         error_description="You don't have permission to access this resource."), 403

# Konfigurasi upload
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'zip', 'rar'}

# Pastikan folder uploads ada
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100MB max file size

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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

def format_file_size(size_bytes):
    """Format ukuran file menjadi format yang mudah dibaca"""
    if size_bytes == 0:
        return "0 B"
    size_names = ["B", "KB", "MB", "GB"]
    i = 0
    while size_bytes >= 1024 and i < len(size_names) - 1:
        size_bytes /= 1024.0
        i += 1
    return f"{size_bytes:.1f} {size_names[i]}"

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

@app.route('/upload', methods=['POST'])
@login_required
def upload_file():
    """Upload file baru - hanya untuk user yang sudah login"""
    if 'file' not in request.files:
        flash('Tidak ada file yang dipilih', 'error')
        return redirect(url_for('index'))
    
    file = request.files['file']
    if file.filename == '':
        flash('Tidak ada file yang dipilih', 'error')
        return redirect(url_for('index'))
    
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
            owner_id=current_user.id,
            team_id=current_user.team_id
        )
        
        db.session.add(file_record)
        db.session.commit()
        
        flash(f'File "{filename}" berhasil diupload oleh {current_user.full_name}!', 'success')
    else:
        flash('Tipe file tidak diizinkan. File yang diizinkan: ' + ', '.join(ALLOWED_EXTENSIONS), 'error')
    
    return redirect(url_for('index'))

@app.route('/download/<filename>')
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
        
        if file_record and os.path.exists(file_record.file_path):
            return send_file(file_record.file_path, as_attachment=True)
        else:
            flash('File tidak ditemukan atau tidak memiliki akses', 'error')
            return redirect(url_for('index'))
    except Exception as e:
        flash(f'Error saat download: {str(e)}', 'error')
        return redirect(url_for('index'))

@app.route('/view/<filename>')
@login_required
def view_file(filename):
    """Preview file (untuk file gambar, text, dan PDF) - hanya untuk user yang sudah login"""
    try:
        if current_user.is_admin:
            # Admin bisa view file dari semua tim
            file_record = File.query.filter_by(stored_name=filename).first()
        else:
            # User biasa hanya bisa view file dari tim mereka
            file_record = File.query.filter_by(
                stored_name=filename, 
                team_id=current_user.team_id
            ).first()
        
        if file_record and os.path.exists(file_record.file_path):
            # Support untuk PDF, gambar, dan text
            if (file_record.mime_type and 
                (file_record.mime_type.startswith(('image/', 'text/')) or 
                 file_record.mime_type == 'application/pdf')):
                return send_file(file_record.file_path)
            else:
                flash('File tidak dapat dipreview', 'error')
                return redirect(url_for('index'))
        else:
            flash('File tidak ditemukan atau tidak memiliki akses', 'error')
            return redirect(url_for('index'))
    except Exception as e:
        flash(f'Error saat preview: {str(e)}', 'error')
        return redirect(url_for('index'))

@app.route('/pdf_viewer/<filename>')
@login_required
def pdf_viewer(filename):
    """Halaman khusus untuk PDF viewer"""
    try:
        if current_user.is_admin:
            # Admin bisa view PDF dari semua tim
            file_record = File.query.filter_by(stored_name=filename).first()
        else:
            # User biasa hanya bisa view PDF dari tim mereka
            file_record = File.query.filter_by(
                stored_name=filename, 
                team_id=current_user.team_id
            ).first()
        
        if file_record and os.path.exists(file_record.file_path):
            if file_record.mime_type == 'application/pdf':
                return render_template('pdf_viewer.html', file=file_record)
            else:
                flash('File bukan PDF', 'error')
                return redirect(url_for('index'))
        else:
            flash('File tidak ditemukan atau tidak memiliki akses', 'error')
            return redirect(url_for('index'))
    except Exception as e:
        flash(f'Error saat membuka PDF: {str(e)}', 'error')
        return redirect(url_for('index'))

@app.route('/delete/<filename>', methods=['POST'])
@login_required
def delete_file(filename):
    """Hapus file - hanya untuk user yang sudah login"""
    try:
        if current_user.is_admin:
            # Admin bisa hapus file dari semua tim
            file_record = File.query.filter_by(stored_name=filename).first()
        else:
            # User biasa hanya bisa hapus file dari tim mereka
            file_record = File.query.filter_by(
                stored_name=filename, 
                team_id=current_user.team_id
            ).first()
        
        if file_record:
            # Hapus file fisik
            if os.path.exists(file_record.file_path):
                os.remove(file_record.file_path)
            
            # Hapus record dari database
            db.session.delete(file_record)
            db.session.commit()
            
            flash(f'File "{file_record.original_name}" berhasil dihapus oleh {current_user.full_name}', 'success')
        else:
            flash('File tidak ditemukan atau tidak memiliki akses', 'error')
    except Exception as e:
        flash(f'Error saat menghapus file: {str(e)}', 'error')
    
    return redirect(url_for('index'))

@app.route('/api/files')
def api_files():
    """API endpoint untuk mendapatkan daftar file"""
    files = get_file_info()
    for file in files:
        file['size_formatted'] = format_file_size(file['size'])
        file['upload_time'] = file['upload_time'].isoformat()
    return jsonify(files)

# Route untuk login
@app.route('/login', methods=['GET', 'POST'])
def login():
    """Halaman login"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Cari user di database
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password) and user.is_active:
            login_user(user)
            # Update last login
            user.last_login = datetime.utcnow()
            db.session.commit()
            
            flash(f'Login berhasil! Selamat datang {user.full_name}!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Username atau password salah!', 'error')
            return render_template('login.html')
    
    # Jika sudah login, redirect ke index
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    return render_template('login.html')

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
def logout():
    """Logout"""
    logout_user()
    flash('Logout berhasil! Terima kasih telah menggunakan Cloud Storage.', 'success')
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    """Dashboard untuk user yang sudah login"""
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)