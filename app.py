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
            print(f"👑 Admin view: {len(files)} files from all teams")
            return files
        else:
            # User biasa hanya bisa melihat file dari tim mereka
            files = File.query.filter_by(team_id=current_user.team_id).order_by(File.created_at.desc()).all()
            print(f"👤 User view: {len(files)} files from team {current_user.team.name if current_user.team else 'Unknown'}")
            return files
    return []

@app.route('/upload', methods=['POST'])
@login_required
def upload_file():
    """Upload file baru - hanya untuk user yang sudah login"""
    try:
        print(f"🔧 Upload request started by user: {current_user.username}")
        print(f"📊 Request method: {request.method}")
        print(f"📊 Request content type: {request.content_type}")
        print(f"📊 Request files: {list(request.files.keys())}")
        
        # Validasi request
        if 'file' not in request.files:
            print("❌ No file in request")
            return jsonify({
                'success': False,
                'error': 'Tidak ada file yang dipilih'
            })
        
        file = request.files['file']
        if not file or file.filename == '':
            print("❌ Empty file")
            return jsonify({
                'success': False,
                'error': 'Tidak ada file yang dipilih'
            })
        
        print(f"📁 File selected: {file.filename}")
        
        # Get file size without reading the entire file
        file.seek(0, 2)  # Seek to end
        file_size = file.tell()
        file.seek(0)  # Reset to beginning
        print(f"📊 File size: {file_size} bytes")
        
        # Validasi ukuran file maksimal 5GB
        max_size = 5 * 1024 * 1024 * 1024  # 5GB
        if file_size > max_size:
            print(f"❌ File too large: {file_size} bytes (max: {max_size} bytes)")
            return jsonify({
                'success': False,
                'error': f'File terlalu besar! Maksimal ukuran file adalah 5GB. Ukuran file Anda: {format_file_size(file_size)}'
            })
        
        # Validasi tipe file
        if not allowed_file(file.filename):
            print(f"❌ File type not allowed: {file.filename}")
            return jsonify({
                'success': False,
                'error': 'Tipe file tidak diizinkan. File yang diizinkan: ' + ', '.join(app.config['ALLOWED_EXTENSIONS'])
            })
        
        # Buat nama file yang aman dan unik
        filename = secure_filename(file.filename)
        if not filename:
            print("❌ Invalid filename after secure_filename")
            return jsonify({
                'success': False,
                'error': 'Nama file tidak valid'
            })
        
        name, ext = os.path.splitext(filename)
        unique_filename = f"{name}_{uuid.uuid4().hex[:8]}{ext}"
        print(f"📝 Generated filename: {unique_filename}")
        
        # Pastikan folder uploads ada
        upload_folder = app.config['UPLOAD_FOLDER']
        if not os.path.exists(upload_folder):
            print(f"📁 Creating upload folder: {upload_folder}")
            os.makedirs(upload_folder, exist_ok=True)
        
        # Simpan file ke folder
        file_path = os.path.join(upload_folder, unique_filename)
        print(f"💾 Saving file to: {file_path}")
        print(f"📁 Upload folder exists: {os.path.exists(upload_folder)}")
        print(f"📁 Upload folder writable: {os.access(upload_folder, os.W_OK)}")
        
        try:
            # Ensure file pointer is at beginning
            file.seek(0)
            file.save(file_path)
            print("✅ File saved successfully")
            
            # Verify file was saved
            if os.path.exists(file_path):
                saved_size = os.path.getsize(file_path)
                print(f"✅ File exists after save, size: {saved_size} bytes")
            else:
                print("❌ File not found after save")
                return jsonify({
                    'success': False,
                    'error': 'File tidak tersimpan ke server'
                })
                
        except Exception as save_error:
            print(f"❌ File save error: {str(save_error)}")
            import traceback
            traceback.print_exc()
            return jsonify({
                'success': False,
                'error': f'Gagal menyimpan file: {str(save_error)}'
            })
        
        # Cek apakah file berhasil disimpan
        if not os.path.exists(file_path):
            print("❌ File not found after save")
            return jsonify({
                'success': False,
                'error': 'Gagal menyimpan file ke server'
            })
        
        # Cek ukuran file
        file_size = os.path.getsize(file_path)
        if file_size == 0:
            print("❌ File size is 0")
            os.remove(file_path)  # Hapus file kosong
            return jsonify({
                'success': False,
                'error': 'File kosong atau rusak'
            })
        
        print(f"📊 File size verified: {file_size} bytes")
        
        # Simpan informasi file ke database
        try:
            file_record = File(
                original_name=filename,
                stored_name=unique_filename,
                file_path=file_path,
                file_size=file_size,
                file_type=ext[1:].lower() if ext else 'unknown',
                mime_type=mimetypes.guess_type(file_path)[0],
                download_key=File().generate_download_key(),
                download_code=File().generate_download_code(),
                owner_id=current_user.id,
                team_id=current_user.team_id
            )
            
            db.session.add(file_record)
            db.session.commit()
            print(f"✅ File record saved to database: ID {file_record.id}")
            
        except Exception as db_error:
            print(f"❌ Database error: {str(db_error)}")
            db.session.rollback()
            # Hapus file jika database error
            if os.path.exists(file_path):
                os.remove(file_path)
            return jsonify({
                'success': False,
                'error': f'Gagal menyimpan ke database: {str(db_error)}'
            })
        
        print(f"✅ Upload completed successfully: {filename} -> {unique_filename}")
        
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
    
    except Exception as e:
        print(f"❌ Upload error: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': f'Error saat upload: {str(e)}'
        })

@app.route('/copy-link/<int:file_id>')
@login_required
def copy_link(file_id):
    """Generate copy link untuk file dengan key yang berganti setiap diklik"""
    try:
        print(f"🔧 Copy link request for file ID: {file_id} by user: {current_user.username}")
        
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
            print(f"❌ File not found or no access: {file_id}")
            return jsonify({
                'success': False,
                'error': 'File tidak ditemukan atau Anda tidak memiliki akses!'
            })
        
        # Generate NEW download key setiap kali copy link
        old_key = file_record.download_key
        new_key = File().generate_download_key()
        new_code = File().generate_download_code()
        
        print(f"🔄 Rotating download key: {old_key} -> {new_key}")
        print(f"🔄 Rotating download code: {file_record.download_code} -> {new_code}")
        
        # Update file record dengan key dan code baru
        file_record.download_key = new_key
        file_record.download_code = new_code
        
        try:
            db.session.commit()
            print(f"✅ Download key and code updated for file: {file_record.original_name}")
        except Exception as db_error:
            print(f"❌ Database error updating keys: {str(db_error)}")
            db.session.rollback()
            return jsonify({
                'success': False,
                'error': f'Gagal mengupdate download key: {str(db_error)}'
            })
        
        # Generate download dan preview URL dengan key baru
        base_url = request.url_root.rstrip('/')
        download_url = f"{base_url}/download/{new_key}"
        preview_url = f"{base_url}/preview/{new_key}"
        
        print(f"🔗 Generated new download URL: {download_url}")
        print(f"🔗 Generated new preview URL: {preview_url}")
        
        return jsonify({
            'success': True,
            'download_url': download_url,
            'preview_url': preview_url,
            'file_name': file_record.original_name,
            'file_type': file_record.file_type,
            'download_code': new_code,
            'message': 'Link download berhasil dibuat dengan key baru!'
        })
        
    except Exception as e:
        print(f"❌ Copy link error: {str(e)}")
        import traceback
        traceback.print_exc()
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
            return render_template('download_error.html', 
                                 error_message="File tidak ditemukan",
                                 error_description="Link download tidak valid atau file sudah dihapus.")
        
        # Cek apakah file ada di filesystem
        if not os.path.exists(file_record.file_path):
            return render_template('download_error.html', 
                                 error_message="File tidak ditemukan",
                                 error_description="File tidak ditemukan di server.")
        
        # Tampilkan halaman verifikasi kode
        return render_template('download_verify.html', 
                             file_record=file_record,
                             download_key=download_key)
        
    except Exception as e:
        print(f"❌ Secure download error: {str(e)}")
        return render_template('download_error.html', 
                             error_message="Error",
                             error_description=f"Terjadi kesalahan: {str(e)}")

@app.route('/verify_download/<download_key>', methods=['POST'])
def verify_download(download_key):
    """Verifikasi kode download"""
    try:
        # Cari file berdasarkan download_key
        file_record = File.query.filter_by(download_key=download_key).first()
        
        if not file_record:
            return jsonify({
                'success': False,
                'error': 'File tidak ditemukan'
            })
        
        # Ambil kode yang dimasukkan user
        entered_code = request.form.get('download_code', '').strip()
        
        # Verifikasi kode
        if entered_code == file_record.download_code:
            # Kode benar, download file
            return send_file(
                file_record.file_path,
                as_attachment=True,
                download_name=file_record.original_name,
                mimetype=file_record.mime_type
            )
        else:
            return jsonify({
                'success': False,
                'error': 'Kode download salah! Silakan coba lagi.'
            })
        
    except Exception as e:
        print(f"❌ Verify download error: {str(e)}")
        return jsonify({
            'success': False,
            'error': f'Error: {str(e)}'
        })

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

@app.route('/get-file-info/<int:file_id>')
@login_required
def get_file_info_by_id(file_id):
    """Get file info by ID - untuk download langsung"""
    try:
        if current_user.is_admin:
            # Admin bisa akses file dari semua tim
            file_record = File.query.get(file_id)
        else:
            # User biasa hanya bisa akses file dari tim mereka
            file_record = File.query.filter_by(
                id=file_id, 
                team_id=current_user.team_id
            ).first()
        
        if not file_record:
            return jsonify({
                'success': False,
                'error': 'File tidak ditemukan atau Anda tidak memiliki akses!'
            })
        
        return jsonify({
            'success': True,
            'file': {
                'id': file_record.id,
                'original_name': file_record.original_name,
                'stored_name': file_record.stored_name,
                'file_type': file_record.file_type,
                'file_size': file_record.file_size,
                'created_at': file_record.created_at.strftime('%d/%m/%Y %H:%M')
            }
        })
        
    except Exception as e:
        print(f"❌ Get file info error: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        })

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


@app.route('/admin/register', methods=['GET', 'POST'])
@login_required
def admin_register():
    """Admin register new user - hanya untuk admin"""
    # Cek apakah user adalah admin
    if not current_user.is_admin:
        flash('Akses ditolak. Hanya admin yang bisa menambah user baru.', 'error')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        try:
            username = request.form['username']
            email = request.form['email']
            full_name = request.form['full_name']
            password = request.form['password']
            team_id = request.form['team_id']
            is_admin = request.form.get('is_admin', '0') == '1'
            
            # Validasi input
            if not username or not email or not full_name or not password or not team_id:
                flash('Semua field harus diisi!', 'error')
                return redirect(url_for('admin_register'))
            
            # Cek apakah username sudah ada
            existing_user = User.query.filter_by(username=username).first()
            if existing_user:
                flash('Username sudah digunakan!', 'error')
                return redirect(url_for('admin_register'))
            
            # Cek apakah email sudah ada
            existing_email = User.query.filter_by(email=email).first()
            if existing_email:
                flash('Email sudah digunakan!', 'error')
                return redirect(url_for('admin_register'))
            
            # Cek apakah team ada
            team = Team.query.get(team_id)
            if not team:
                flash('Tim tidak ditemukan!', 'error')
                return redirect(url_for('admin_register'))
            
            # Buat user baru
            new_user = User(
                username=username,
                email=email,
                full_name=full_name,
                team_id=team_id,
                is_admin=is_admin
            )
            new_user.set_password(password)
            
            db.session.add(new_user)
            db.session.commit()
            
            flash(f'User "{username}" berhasil ditambahkan!', 'success')
            return redirect(url_for('index'))
            
        except Exception as e:
            print(f"❌ Admin register error: {str(e)}")
            flash(f'Error saat menambah user: {str(e)}', 'error')
            return redirect(url_for('admin_register'))
    
    # GET request - tampilkan form
    try:
        teams = Team.query.all()
        return render_template('admin_register.html', teams=teams)
    except Exception as e:
        print(f"❌ Admin register page error: {str(e)}")
        flash(f'Error loading admin register page: {str(e)}', 'error')
        return render_template('error.html', 
                             error_code=500, 
                             error_message="Admin Register Page Error",
                             error_description="Unable to load admin register page. Please try again later."), 500

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
