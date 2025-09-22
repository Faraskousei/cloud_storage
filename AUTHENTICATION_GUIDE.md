# 🔐 Panduan Authentication & Role Management

## 📋 Ringkasan Sistem

Sistem cloud storage telah ditingkatkan dengan **authentication dan role management** yang lengkap, menggunakan database MySQL untuk menyimpan data user, team, dan file dengan isolasi per tim.

## 🏗️ **Arsitektur Sistem**

### **Database Structure**
```
cloud_storage/
├── teams (3 tim default)
├── users (dengan role admin/user)
└── files (dengan team isolation)
```

### **3 Teams Default**
1. **Team Development** (Hijau) - Tim pengembangan aplikasi
2. **Team Marketing** (Kuning) - Tim marketing dan promosi  
3. **Team Operations** (Ungu) - Tim operasional dan support

### **Role System**
- **Admin**: Dapat akses semua file, register user baru, manage teams
- **User**: Hanya dapat akses file dari team mereka sendiri

## 🚀 **Cara Setup & Instalasi**

### **1. Persiapan XAMPP**
```bash
# Pastikan XAMPP MySQL running
1. Buka XAMPP Control Panel
2. Start MySQL service
3. Buka phpMyAdmin (http://localhost/phpmyadmin)
```

### **2. Setup Database**
```bash
# Import database schema
mysql -u root -p < setup_database.sql

# Atau manual di phpMyAdmin:
# - Buat database 'cloud_storage'
# - Import file setup_database.sql
```

### **3. Install & Run**
```bash
# Windows - Cara Cepat
double-click setup_with_auth.bat

# Manual
pip install -r requirements.txt
python main.py
```

## 👤 **Login Credentials**

### **Admin Account**
- **Username**: `admin`
- **Password**: `admin123`
- **Team**: Development
- **Role**: Administrator

### **Demo Teams**
- **Development**: Tim pengembangan (Hijau)
- **Marketing**: Tim marketing (Kuning)
- **Operations**: Tim operasional (Ungu)

## 🔐 **Fitur Authentication**

### **1. Login System**
- ✅ Username/Email login
- ✅ Password hashing dengan Werkzeug
- ✅ Remember me functionality
- ✅ Session management
- ✅ Auto-redirect setelah login

### **2. Registration (Admin Only)**
- ✅ Hanya admin yang dapat register user baru
- ✅ Form validation lengkap
- ✅ Team assignment
- ✅ Email uniqueness check

### **3. Profile Management**
- ✅ View profile information
- ✅ Change password dengan strength indicator
- ✅ Team info display
- ✅ Login history

### **4. Security Features**
- ✅ Password strength validation
- ✅ CSRF protection
- ✅ SQL injection protection
- ✅ XSS protection

## 🎯 **Role-Based Access Control**

### **Admin Permissions**
- ✅ Akses semua file dari semua team
- ✅ Register user baru
- ✅ View team statistics
- ✅ Manage users dan teams
- ✅ Full system access

### **User Permissions**
- ✅ Hanya akses file dari team mereka
- ✅ Upload file ke team folder
- ✅ Download file team mereka
- ✅ Preview file team mereka
- ✅ Manage profile sendiri

## 📁 **File Isolation System**

### **Folder Structure**
```
uploads/
├── team_1/ (Development)
├── team_2/ (Marketing)
└── team_3/ (Operations)
```

### **Database Isolation**
- ✅ File records dengan team_id
- ✅ Query filtering berdasarkan team
- ✅ Access control di level database
- ✅ Owner tracking per file

## 🎨 **UI/UX Features**

### **1. Enhanced Navigation**
- ✅ User dropdown dengan team badge
- ✅ Role-based menu items
- ✅ Team color coding
- ✅ Admin indicators

### **2. Dashboard per Team**
- ✅ Team-specific file listing
- ✅ Team statistics
- ✅ Admin overview (jika admin)
- ✅ File isolation display

### **3. Login Interface**
- ✅ Modern login form
- ✅ Demo credentials display
- ✅ Password visibility toggle
- ✅ Remember me option

### **4. Registration Interface**
- ✅ Team selection dengan color preview
- ✅ Form validation
- ✅ Password strength indicator
- ✅ Real-time feedback

## 🔧 **Technical Implementation**

### **1. Models (models.py)**
```python
- User: UserMixin untuk Flask-Login
- Team: Team management
- File: File dengan team isolation
```

### **2. Authentication (auth.py)**
```python
- Login/logout routes
- Registration routes
- Password management
- Access control decorators
```

### **3. Main App (main.py)**
```python
- Dashboard dengan team filtering
- File upload dengan team isolation
- Download/view dengan access control
- Admin management routes
```

### **4. Configuration**
```python
- MySQL connection settings
- Flask-Login configuration
- Security settings
- Database initialization
```

## 📊 **Database Schema**

### **Teams Table**
```sql
CREATE TABLE teams (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
    description TEXT,
    color VARCHAR(7) DEFAULT '#6366f1',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### **Users Table**
```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(80) UNIQUE NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    is_admin BOOLEAN DEFAULT FALSE,
    team_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP NULL
);
```

### **Files Table**
```sql
CREATE TABLE files (
    id INT AUTO_INCREMENT PRIMARY KEY,
    original_name VARCHAR(255) NOT NULL,
    stored_name VARCHAR(255) NOT NULL,
    file_path VARCHAR(500) NOT NULL,
    file_size BIGINT NOT NULL,
    file_type VARCHAR(50) NOT NULL,
    owner_id INT NOT NULL,
    team_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 🛡️ **Security Measures**

### **1. Password Security**
- ✅ Werkzeug password hashing
- ✅ Salted passwords
- ✅ Password strength validation
- ✅ Secure password storage

### **2. Access Control**
- ✅ Team-based file isolation
- ✅ Role-based permissions
- ✅ Session management
- ✅ CSRF protection

### **3. Data Validation**
- ✅ Input sanitization
- ✅ SQL injection prevention
- ✅ XSS protection
- ✅ File type validation

## 📱 **Responsive Design**

### **Mobile Features**
- ✅ Touch-friendly login
- ✅ Responsive dashboard
- ✅ Mobile navigation
- ✅ Touch file management

### **Desktop Features**
- ✅ Full feature access
- ✅ Keyboard shortcuts
- ✅ Drag & drop upload
- ✅ Multi-window support

## 🎯 **Usage Examples**

### **1. Login sebagai Admin**
```
1. Buka http://localhost:5000
2. Login dengan admin/admin123
3. Akses semua fitur admin
4. Register user baru
5. View semua file dari semua team
```

### **2. Login sebagai User**
```
1. Login dengan user yang dibuat admin
2. Hanya lihat file dari team mereka
3. Upload file ke team folder
4. Manage profile sendiri
```

### **3. Team Isolation**
```
- Development team: Hanya lihat file team_1/
- Marketing team: Hanya lihat file team_2/
- Operations team: Hanya lihat file team_3/
- Admin: Lihat semua file dari semua team
```

## 🚀 **Deployment Notes**

### **Production Setup**
1. **Environment Variables**:
   ```bash
   export MYSQL_HOST=your_host
   export MYSQL_USER=your_user
   export MYSQL_PASSWORD=your_password
   export SECRET_KEY=your_secret_key
   ```

2. **Database Security**:
   - Gunakan user MySQL terpisah
   - Enable SSL connection
   - Regular backups

3. **Application Security**:
   - Use HTTPS
   - Set secure session cookies
   - Enable CSRF protection

## 📋 **Troubleshooting**

### **Common Issues**

1. **Database Connection Error**
   ```bash
   # Check MySQL service running
   # Verify credentials in config.py
   # Check firewall settings
   ```

2. **Login Issues**
   ```bash
   # Verify user exists in database
   # Check password hash
   # Clear browser cache
   ```

3. **File Upload Issues**
   ```bash
   # Check upload folder permissions
   # Verify file size limits
   # Check disk space
   ```

## 🎉 **Hasil Akhir**

Sistem cloud storage sekarang memiliki:

✅ **Complete Authentication System**  
✅ **3 Teams dengan Role Management**  
✅ **File Isolation per Team**  
✅ **Admin & User Permissions**  
✅ **MySQL Database Integration**  
✅ **Modern UI/UX**  
✅ **Security Features**  
✅ **Responsive Design**  

**Total fitur baru: 20+ fitur authentication dan role management!** 🚀

---

**Selamat menggunakan sistem cloud storage dengan authentication!** 🎉
