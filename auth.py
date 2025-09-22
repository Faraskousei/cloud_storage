from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_login import login_user, logout_user, login_required, current_user
from models import db, User, Team
from werkzeug.security import check_password_hash
import re

auth_bp = Blueprint('auth', __name__)

def validate_email(email):
    """Validasi format email"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_password(password):
    """Validasi password (minimal 6 karakter)"""
    return len(password) >= 6

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Halaman login"""
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        remember = bool(request.form.get('remember'))
        
        # Validasi input
        if not username or not password:
            flash('Username dan password harus diisi', 'error')
            return render_template('auth/login.html')
        
        # Cari user berdasarkan username atau email
        user = User.query.filter(
            (User.username == username) | (User.email == username)
        ).first()
        
        if user and user.check_password(password) and user.is_active:
            # Update last login
            from datetime import datetime
            user.last_login = datetime.utcnow()
            db.session.commit()
            
            # Login user
            login_user(user, remember=remember)
            
            # Set team info di session
            session['team_id'] = user.team_id
            session['team_name'] = user.get_team_name()
            session['team_color'] = user.get_team_color()
            session['is_admin'] = user.is_admin
            
            flash(f'Selamat datang, {user.full_name}!', 'success')
            
            # Redirect ke dashboard
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.dashboard'))
        else:
            flash('Username/email atau password salah', 'error')
    
    return render_template('auth/login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """Halaman registrasi (hanya untuk admin)"""
    if not current_user.is_authenticated or not current_user.is_admin:
        flash('Akses ditolak. Hanya admin yang dapat mendaftarkan user baru.', 'error')
        return redirect(url_for('auth.login'))
    
    teams = Team.query.all()
    
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')
        full_name = request.form.get('full_name', '').strip()
        team_id = request.form.get('team_id')
        
        # Validasi input
        errors = []
        
        if not username:
            errors.append('Username harus diisi')
        elif len(username) < 3:
            errors.append('Username minimal 3 karakter')
        elif User.query.filter_by(username=username).first():
            errors.append('Username sudah digunakan')
        
        if not email:
            errors.append('Email harus diisi')
        elif not validate_email(email):
            errors.append('Format email tidak valid')
        elif User.query.filter_by(email=email).first():
            errors.append('Email sudah digunakan')
        
        if not password:
            errors.append('Password harus diisi')
        elif not validate_password(password):
            errors.append('Password minimal 6 karakter')
        elif password != confirm_password:
            errors.append('Password dan konfirmasi password tidak sama')
        
        if not full_name:
            errors.append('Nama lengkap harus diisi')
        
        if not team_id:
            errors.append('Team harus dipilih')
        elif not Team.query.get(team_id):
            errors.append('Team tidak valid')
        
        if errors:
            for error in errors:
                flash(error, 'error')
        else:
            # Buat user baru
            try:
                new_user = User(
                    username=username,
                    email=email,
                    full_name=full_name,
                    team_id=int(team_id)
                )
                new_user.set_password(password)
                
                db.session.add(new_user)
                db.session.commit()
                
                flash(f'User {username} berhasil didaftarkan!', 'success')
                return redirect(url_for('auth.register'))
                
            except Exception as e:
                db.session.rollback()
                flash(f'Error saat mendaftarkan user: {str(e)}', 'error')
    
    return render_template('auth/register.html', teams=teams)

@auth_bp.route('/logout')
@login_required
def logout():
    """Logout user"""
    user_name = current_user.full_name
    logout_user()
    session.clear()
    flash(f'Sampai jumpa, {user_name}!', 'info')
    return redirect(url_for('auth.login'))

@auth_bp.route('/profile')
@login_required
def profile():
    """Halaman profil user"""
    return render_template('auth/profile.html')

@auth_bp.route('/change-password', methods=['GET', 'POST'])
@login_required
def change_password():
    """Ubah password"""
    if request.method == 'POST':
        current_password = request.form.get('current_password', '')
        new_password = request.form.get('new_password', '')
        confirm_password = request.form.get('confirm_password', '')
        
        # Validasi
        if not current_password or not current_user.check_password(current_password):
            flash('Password lama salah', 'error')
            return render_template('auth/change_password.html')
        
        if not new_password:
            flash('Password baru harus diisi', 'error')
            return render_template('auth/change_password.html')
        
        if not validate_password(new_password):
            flash('Password baru minimal 6 karakter', 'error')
            return render_template('auth/change_password.html')
        
        if new_password != confirm_password:
            flash('Password baru dan konfirmasi tidak sama', 'error')
            return render_template('auth/change_password.html')
        
        # Update password
        try:
            current_user.set_password(new_password)
            db.session.commit()
            flash('Password berhasil diubah!', 'success')
            return redirect(url_for('auth.profile'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error saat mengubah password: {str(e)}', 'error')
    
    return render_template('auth/change_password.html')

def require_admin(f):
    """Decorator untuk memerlukan akses admin"""
    from functools import wraps
    
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            return redirect(url_for('auth.login'))
        if not current_user.is_admin:
            flash('Akses ditolak. Anda tidak memiliki permission admin.', 'error')
            return redirect(url_for('main.dashboard'))
        return f(*args, **kwargs)
    return decorated_function

def require_team_access(team_id=None):
    """Decorator untuk memerlukan akses team tertentu"""
    from functools import wraps
    
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated:
                return redirect(url_for('auth.login'))
            
            # Admin dapat akses semua team
            if current_user.is_admin:
                return f(*args, **kwargs)
            
            # User biasa hanya dapat akses team mereka
            if team_id and current_user.team_id != team_id:
                flash('Akses ditolak. Anda tidak memiliki akses ke team ini.', 'error')
                return redirect(url_for('main.dashboard'))
            
            return f(*args, **kwargs)
        return decorated_function
    return decorator
