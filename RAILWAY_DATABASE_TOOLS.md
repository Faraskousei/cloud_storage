# 🗄️ Railway Database Tools

## 📋 Database Management Tools untuk Railway PostgreSQL

### 🎯 **Tujuan:**
- Dump database dari Railway PostgreSQL
- Restore database ke Railway PostgreSQL
- Backup database Railway
- Manage database operations

---

## 🔧 **Tools yang Tersedia:**

### **1. dump_db.py - Database Dump Tool**
```bash
# Full database dump (schema + data)
python dump_db.py full

# Data-only dump
python dump_db.py data

# List available dump files
python dump_db.py list
```

### **2. restore_db.py - Database Restore Tool**
```bash
# Restore from dump file
python restore_db.py dump_file.sql

# List and select dump file
python restore_db.py
```

### **3. backup_railway.py - Database Backup Tool**
```bash
# Create backup
python backup_railway.py backup

# List backup files
python backup_railway.py list

# Cleanup old backups (older than 30 days)
python backup_railway.py cleanup 30
```

---

## 🚀 **Setup dan Instalasi:**

### **1. Install PostgreSQL Tools**
```bash
# Windows (using Chocolatey)
choco install postgresql

# Windows (using Scoop)
scoop install postgresql

# Linux (Ubuntu/Debian)
sudo apt-get install postgresql-client

# macOS (using Homebrew)
brew install postgresql
```

### **2. Verify Installation**
```bash
# Check pg_dump version
pg_dump --version

# Check psql version
psql --version
```

---

## 🔧 **Penggunaan Tools:**

### **1. Database Dump**

#### **Full Database Dump:**
```bash
python dump_db.py full
```
- **Output:** `database_dumps/railway_dump_YYYYMMDD_HHMMSS.sql`
- **Contains:** Schema + Data
- **Use case:** Complete database backup

#### **Data-Only Dump:**
```bash
python dump_db.py data
```
- **Output:** `database_dumps/railway_data_YYYYMMDD_HHMMSS.sql`
- **Contains:** Data only
- **Use case:** Data migration

#### **List Dump Files:**
```bash
python dump_db.py list
```
- **Shows:** Available dump files with size and timestamp

### **2. Database Restore**

#### **Restore from File:**
```bash
python restore_db.py dump_file.sql
```
- **Input:** Dump file path
- **Action:** Restore database from dump file

#### **Interactive Restore:**
```bash
python restore_db.py
```
- **Shows:** List of available dump files
- **Select:** Choose file to restore

### **3. Database Backup**

#### **Create Backup:**
```bash
python backup_railway.py backup
```
- **Output:** `railway_backups/railway_backup_YYYYMMDD_HHMMSS.sql`
- **Info:** `railway_backups/backup_info_YYYYMMDD_HHMMSS.json`

#### **List Backups:**
```bash
python backup_railway.py list
```
- **Shows:** Available backup files with details

#### **Cleanup Old Backups:**
```bash
python backup_railway.py cleanup 30
```
- **Action:** Remove backups older than 30 days
- **Parameter:** Number of days to keep

---

## 📁 **File Structure:**

### **Database Dumps:**
```
database_dumps/
├── railway_dump_20250122_143022.sql
├── railway_dump_20250122_150145.sql
└── railway_data_20250122_151200.sql
```

### **Railway Backups:**
```
railway_backups/
├── railway_backup_20250122_143022.sql
├── backup_info_20250122_143022.json
└── railway_backup_20250122_150145.sql
```

---

## 🔧 **Konfigurasi:**

### **1. Environment Variables:**
```bash
# Railway will auto-provide
DATABASE_URL=postgresql://postgres:password@host:port/railway

# Or set manually
FLASK_ENV=production
```

### **2. Database Connection:**
- **Host:** Railway PostgreSQL host
- **Port:** Railway PostgreSQL port
- **Database:** Railway database name
- **User:** Railway database user
- **Password:** Railway database password

---

## 🚀 **Railway Integration:**

### **1. Automatic Detection:**
- **DATABASE_URL** dari Railway environment
- **Production config** untuk Railway
- **PostgreSQL connection** otomatis

### **2. Connection Details:**
```python
# Railway DATABASE_URL format
postgresql://postgres:password@host:port/railway

# Extracted details
host = "turntable.proxy.rlwy.net"
port = "32722"
database = "railway"
user = "postgres"
password = "pzwHnzfmqcgvILIojOKbcvxUcQXMzInL"
```

---

## 📋 **Contoh Penggunaan:**

### **1. Backup Database:**
```bash
# Create backup
python backup_railway.py backup

# Output:
# ✅ Database backup completed successfully!
# 📁 Backup saved to: railway_backups/railway_backup_20250122_143022.sql
# 📊 Backup size: 15,432 bytes
```

### **2. Dump Database:**
```bash
# Full dump
python dump_db.py full

# Output:
# ✅ Database dump completed successfully!
# 📁 Dump saved to: database_dumps/railway_dump_20250122_143022.sql
# 📊 Dump size: 15,432 bytes
```

### **3. Restore Database:**
```bash
# Restore from file
python restore_db.py database_dumps/railway_dump_20250122_143022.sql

# Output:
# ✅ Database restore completed successfully!
# 🌐 Check your Railway application to verify the restore
```

---

## 🔧 **Troubleshooting:**

### **Common Issues:**

#### **1. pg_dump not found:**
```bash
# Install PostgreSQL client tools
# Windows: choco install postgresql
# Linux: sudo apt-get install postgresql-client
# macOS: brew install postgresql
```

#### **2. Connection refused:**
```bash
# Check Railway database status
# Verify DATABASE_URL in Railway dashboard
# Check network connectivity
```

#### **3. Permission denied:**
```bash
# Check file permissions
# Ensure backup directory is writable
# Verify database user permissions
```

### **Debug Commands:**
```bash
# Test database connection
python -c "from app import app; print(app.config['SQLALCHEMY_DATABASE_URI'])"

# Test pg_dump
pg_dump --version

# Test psql
psql --version
```

---

## 📞 **Support:**

### **Documentation:**
- **PostgreSQL Docs:** https://www.postgresql.org/docs/
- **Railway Docs:** https://docs.railway.app
- **pg_dump Docs:** https://www.postgresql.org/docs/current/app-pgdump.html

### **Tools:**
- **dump_db.py** - Database dump tool
- **restore_db.py** - Database restore tool
- **backup_railway.py** - Database backup tool

---

## 🎉 **Success Checklist:**

### **✅ Setup Checklist:**
- [ ] PostgreSQL client tools installed
- [ ] Railway database accessible
- [ ] DATABASE_URL configured
- [ ] Backup directory created
- [ ] Tools tested

### **✅ Usage Checklist:**
- [ ] Database backup created
- [ ] Database dump created
- [ ] Database restore tested
- [ ] Old backups cleaned up
- [ ] Railway application verified

---

**Database tools ready! Manage your Railway PostgreSQL database with ease. 🚀✨**
