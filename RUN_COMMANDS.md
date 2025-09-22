# 🚀 Command untuk Menjalankan Cloud Storage

## 📋 **Langkah-langkah Setup & Run**

### **1. Persiapan XAMPP MySQL**

```bash
# Buka XAMPP Control Panel
# Start MySQL service
# Buka phpMyAdmin di browser: http://localhost/phpmyadmin
```

### **2. Setup Database MySQL**

```bash
# Method 1: Import via phpMyAdmin
# 1. Buka http://localhost/phpmyadmin
# 2. Buat database baru dengan nama: cloud_storage
# 3. Import file setup_database.sql

# Method 2: Via Command Line
mysql -u root -p
# Masukkan password MySQL (default: kosong)
# Kemudian jalankan:
SOURCE setup_database.sql;
# Atau:
mysql -u root -p cloud_storage < setup_database.sql
```

### **3. Install Dependencies Python**

```bash
# Buat virtual environment (jika belum ada)
python -m venv venv

# Aktifkan virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

### **4. Run Application**

```bash
# Method 1: Menggunakan main.py (Recommended)
python main.py

# Method 2: Menggunakan run.py (Legacy)
python run.py

# Method 3: Menggunakan setup script (Windows)
setup_with_auth.bat
```

## 🎯 **Command Lengkap (Copy-Paste Ready)**

### **Windows PowerShell/CMD:**

```powershell
# 1. Setup Database
mysql -u root -p
# (Masukkan password, default kosong)
SOURCE setup_database.sql;
exit;

# 2. Setup Python Environment
python -m venv venv
venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt

# 3. Run Application
python main.py
```

### **Linux/Mac Terminal:**

```bash
# 1. Setup Database
mysql -u root -p
# (Masukkan password)
SOURCE setup_database.sql;
exit;

# 2. Setup Python Environment
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# 3. Run Application
python main.py
```

## 🔧 **Troubleshooting Commands**

### **Jika Database Error:**

```bash
# Check MySQL service
# Windows:
net start mysql
# Linux:
sudo systemctl start mysql

# Test connection
mysql -u root -p -e "SHOW DATABASES;"

# Recreate database
mysql -u root -p -e "DROP DATABASE IF EXISTS cloud_storage;"
mysql -u root -p -e "CREATE DATABASE cloud_storage;"
mysql -u root -p cloud_storage < setup_database.sql
```

### **Jika Python Dependencies Error:**

```bash
# Clear pip cache
pip cache purge

# Reinstall dependencies
pip uninstall -r requirements.txt -y
pip install -r requirements.txt

# Check Python version
python --version
# Harus Python 3.7+
```

### **Jika Port 5000 Busy:**

```bash
# Check port usage
# Windows:
netstat -ano | findstr :5000
# Linux:
lsof -i :5000

# Kill process using port 5000
# Windows:
taskkill /PID <PID_NUMBER> /F
# Linux:
kill -9 <PID_NUMBER>

# Atau ubah port di main.py
# Ganti port=5000 menjadi port=8080
```

## 🎮 **Quick Start Commands**

### **One-Line Setup (Windows):**

```powershell
# Setup database dan run aplikasi
mysql -u root -p < setup_database.sql && python -m venv venv && venv\Scripts\activate && pip install -r requirements.txt && python main.py
```

### **One-Line Setup (Linux/Mac):**

```bash
# Setup database dan run aplikasi
mysql -u root -p < setup_database.sql && python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt && python main.py
```

## 📱 **Access Application**

```bash
# Setelah aplikasi running, buka browser:
http://localhost:5000

# Login credentials:
# Username: admin
# Password: admin123
# Team: Development (Hijau)
```

## 🔍 **Verification Commands**

### **Check Database:**

```sql
-- Login ke MySQL
mysql -u root -p cloud_storage

-- Check tables
SHOW TABLES;

-- Check teams
SELECT * FROM teams;

-- Check users
SELECT username, email, full_name, is_admin, team_id FROM users;

-- Check files (jika ada)
SELECT f.original_name, t.name as team, u.full_name as owner 
FROM files f 
JOIN teams t ON f.team_id = t.id 
JOIN users u ON f.owner_id = u.id;
```

### **Check Application Logs:**

```bash
# Monitor application logs
# Aplikasi akan menampilkan log di terminal
# Look for:
# ✅ Database initialized with default teams and admin user
# ✅ Cloud Storage Server dimulai...
# ✅ Running on http://0.0.0.0:5000
```

## 🚨 **Common Issues & Solutions**

### **Issue 1: MySQL Connection Error**
```bash
# Solution: Check XAMPP MySQL service
# 1. Buka XAMPP Control Panel
# 2. Start MySQL service
# 3. Test connection: mysql -u root -p
```

### **Issue 2: Python Module Not Found**
```bash
# Solution: Install missing modules
pip install Flask Flask-SQLAlchemy Flask-Login PyMySQL
```

### **Issue 3: Port 5000 Already in Use**
```bash
# Solution: Change port in main.py
# Edit line: app.run(debug=True, host='0.0.0.0', port=5000)
# Change to: app.run(debug=True, host='0.0.0.0', port=8080)
```

### **Issue 4: Database Permission Error**
```bash
# Solution: Grant permissions
mysql -u root -p
GRANT ALL PRIVILEGES ON cloud_storage.* TO 'root'@'localhost';
FLUSH PRIVILEGES;
```

## 🎯 **Final Verification**

### **Check All Services Running:**

```bash
# 1. MySQL Service
mysql -u root -p -e "SELECT 1;"

# 2. Python Application
curl http://localhost:5000
# Should return HTML page

# 3. Database Tables
mysql -u root -p cloud_storage -e "SELECT COUNT(*) as team_count FROM teams;"
# Should return: 3

# 4. Admin User
mysql -u root -p cloud_storage -e "SELECT username FROM users WHERE is_admin=1;"
# Should return: admin
```

## 🎉 **Success Indicators**

Jika semua berjalan dengan baik, Anda akan melihat:

```bash
✅ Database initialized with default teams and admin user
📧 Admin credentials: username='admin', password='admin123'
👥 Teams created: Development, Marketing, Operations
🚀 Cloud Storage Server dimulai...
📁 Upload folder: C:\Users\...\uploads
🌐 Akses aplikasi di: http://localhost:5000
⏹️  Tekan Ctrl+C untuk menghentikan server
```

**Selamat! Sistem cloud storage dengan authentication siap digunakan! 🎉**
