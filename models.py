from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import os

db = SQLAlchemy()

class Team(db.Model):
    """Model untuk tim/role"""
    __tablename__ = 'teams'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.Text)
    color = db.Column(db.String(7), default='#6366f1')  # Hex color untuk UI
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationship dengan users
    users = db.relationship('User', backref='team', lazy=True)
    
    def __repr__(self):
        return f'<Team {self.name}>'

class User(UserMixin, db.Model):
    """Model untuk user dengan role/team"""
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime)
    
    # Foreign key ke Team
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    
    # Relationship dengan files
    files = db.relationship('File', backref='owner', lazy=True)
    
    def set_password(self, password):
        """Set password dengan hash"""
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """Check password"""
        return check_password_hash(self.password_hash, password)
    
    def get_team_name(self):
        """Get nama tim"""
        return self.team.name if self.team else None
    
    def get_team_color(self):
        """Get warna tim"""
        return self.team.color if self.team else '#6366f1'
    
    def __repr__(self):
        return f'<User {self.username}>'

class File(db.Model):
    """Model untuk file dengan team isolation"""
    __tablename__ = 'files'
    
    id = db.Column(db.Integer, primary_key=True)
    original_name = db.Column(db.String(255), nullable=False)
    stored_name = db.Column(db.String(255), nullable=False)
    file_path = db.Column(db.String(500), nullable=False)
    file_size = db.Column(db.BigInteger, nullable=False)
    file_type = db.Column(db.String(50), nullable=False)
    mime_type = db.Column(db.String(100))
    description = db.Column(db.Text)
    is_public = db.Column(db.Boolean, default=False)
    download_key = db.Column(db.String(32), unique=True, nullable=False)  # Unique key untuk download
    download_code = db.Column(db.String(6), nullable=False)  # 6-digit code untuk download
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Foreign keys
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    
    # Relationships
    team = db.relationship('Team', backref='files')
    
    def format_file_size(self):
        """Format ukuran file"""
        if self.file_size == 0:
            return "0 B"
        size_names = ["B", "KB", "MB", "GB"]
        i = 0
        size = float(self.file_size)
        while size >= 1024 and i < len(size_names) - 1:
            size /= 1024.0
            i += 1
        return f"{size:.1f} {size_names[i]}"
    
    def get_file_extension(self):
        """Get extension file"""
        return self.original_name.rsplit('.', 1)[1].lower() if '.' in self.original_name else 'unknown'
    
    def generate_download_key(self):
        """Generate unique download key"""
        import secrets
        return secrets.token_urlsafe(24)
    
    def generate_download_code(self):
        """Generate 6-digit download code"""
        import random
        return f"{random.randint(100000, 999999)}"
    
    def get_download_url(self, base_url):
        """Get secure download URL"""
        return f"{base_url}/download/{self.download_key}"
    
    def get_preview_url(self, base_url):
        """Get secure preview URL"""
        return f"{base_url}/preview/{self.download_key}"
    
    def __repr__(self):
        return f'<File {self.original_name}>'

def init_database(app):
    """Initialize database dengan data default"""
    with app.app_context():
        # Create tables
        db.create_all()
        
        # Check jika sudah ada data
        if Team.query.first() is None:
            # Create default teams
            teams_data = [
                {'name': 'Team Development', 'description': 'Tim untuk pengembangan aplikasi', 'color': '#10b981'},
                {'name': 'Team Marketing', 'description': 'Tim untuk marketing dan promosi', 'color': '#f59e0b'},
                {'name': 'Team Operations', 'description': 'Tim untuk operasional dan support', 'color': '#8b5cf6'}
            ]
            
            for team_data in teams_data:
                team = Team(**team_data)
                db.session.add(team)
            
            db.session.commit()
            
            # Create admin users
            admin_team = Team.query.filter_by(name='Team Development').first()
            if admin_team:
                # Admin user 1
                admin_user = User(
                    username='admin',
                    email='admin@company.com',
                    full_name='System Administrator',
                    team_id=admin_team.id,
                    is_admin=True
                )
                admin_user.set_password('admin123')
                db.session.add(admin_user)
                
                # Admin user 2 - frxadz
                frxadz_user = User(
                    username='frxadz',
                    email='frxadz@company.com',
                    full_name='Frxadz Administrator',
                    team_id=admin_team.id,
                    is_admin=True
                )
                frxadz_user.set_password('admin')
                db.session.add(frxadz_user)
                
                db.session.commit()
                
                print("✅ Database initialized with default teams and admin users")
                print("📧 Admin credentials:")
                print("   - username='admin', password='admin123'")
                print("   - username='frxadz', password='admin'")
                print("👥 Teams created: Development, Marketing, Operations")
