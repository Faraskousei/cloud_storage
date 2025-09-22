# 🌐 NGROK Tutorial - Cloud Storage

## 📋 Panduan Lengkap Menggunakan NGROK

### 🎯 **Tujuan:**
- Menjalankan aplikasi Cloud Storage dengan NGROK
- Mengakses aplikasi dari internet
- Sharing aplikasi dengan orang lain
- Testing aplikasi di berbagai device

---

## 🔧 **Langkah 1: Install NGROK**

### **1.1 Download NGROK**
1. **Go to:** https://ngrok.com/download
2. **Download** untuk Windows
3. **Extract** file ngrok.exe ke folder yang mudah diakses
4. **Contoh:** `C:\ngrok\ngrok.exe`

### **1.2 Alternative - Using Chocolatey**
```bash
# Install Chocolatey (if not installed)
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Install NGROK
choco install ngrok
```

### **1.3 Alternative - Using Scoop**
```bash
# Install Scoop (if not installed)
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
irm get.scoop.sh | iex

# Install NGROK
scoop install ngrok
```

---

## 🚀 **Langkah 2: Setup NGROK Account**

### **2.1 Create Account**
1. **Go to:** https://ngrok.com
2. **Sign up** dengan email
3. **Verify** email address
4. **Login** ke dashboard

### **2.2 Get Auth Token**
1. **Go to:** https://dashboard.ngrok.com/get-started/your-authtoken
2. **Copy** authtoken Anda
3. **Contoh:** `2abc123def456ghi789jkl012mno345pqr678stu901vwx234yz567`

### **2.3 Configure NGROK**
```bash
# Set authtoken
ngrok config add-authtoken YOUR_AUTHTOKEN_HERE

# Verify configuration
ngrok config check
```

---

## 🔧 **Langkah 3: Run Application dengan NGROK**

### **3.1 Start Flask Application**
```bash
# Terminal 1 - Start Flask app
cd C:\xampp\htdocs\CLOUD_TEST
venv\Scripts\python.exe run.py
```

### **3.2 Start NGROK**
```bash
# Terminal 2 - Start NGROK
ngrok http 5000
```

### **3.3 Alternative - One Command**
```bash
# Start both Flask and NGROK
start "Flask App" cmd /k "venv\Scripts\python.exe run.py"
timeout /t 3
start "NGROK" cmd /k "ngrok http 5000"
```

---

## 🌐 **Langkah 4: Access Application**

### **4.1 NGROK Output**
```
ngrok                                                                               

Session Status                online
Account                       your-email@example.com
Version                       3.x.x
Region                        United States (us)
Latency                       45ms
Web Interface                 http://127.0.0.1:4040
Forwarding                    https://abc123.ngrok-free.app -> http://localhost:5000
Forwarding                    http://abc123.ngrok-free.app -> http://localhost:5000

Connections                   ttl     opn     rt1     rt5     p50     p90
                              0       0       0.00    0.00    0.00    0.00
```

### **4.2 Access URLs**
- **HTTPS:** `https://abc123.ngrok-free.app`
- **HTTP:** `http://abc123.ngrok-free.app`
- **Local:** `http://localhost:5000`

---

## 🔧 **Langkah 5: Advanced NGROK Configuration**

### **5.1 Custom Subdomain**
```bash
# Start with custom subdomain
ngrok http 5000 --subdomain=my-cloud-storage
```

### **5.2 Custom Domain**
```bash
# Start with custom domain
ngrok http 5000 --hostname=myapp.example.com
```

### **5.3 Authentication**
```bash
# Start with basic auth
ngrok http 5000 --basic-auth="username:password"
```

### **5.4 Custom Headers**
```bash
# Start with custom headers
ngrok http 5000 --host-header="localhost:5000"
```

---

## 📋 **Langkah 6: NGROK Web Interface**

### **6.1 Access Web Interface**
- **URL:** `http://127.0.0.1:4040`
- **Features:** Request inspection, replay, monitoring

### **6.2 Features Available**
- **Request History** - Lihat semua request
- **Request Details** - Headers, body, response
- **Replay Requests** - Replay request untuk testing
- **Export Data** - Export request data

---

## 🔧 **Langkah 7: Batch Scripts untuk Automation**

### **7.1 Start App with NGROK**
```batch
@echo off
echo ========================================
echo   Start Cloud Storage with NGROK
echo ========================================
echo.

echo 🔧 Starting Flask application...
start "Flask App" cmd /k "venv\Scripts\python.exe run.py"

echo ⏳ Waiting for Flask to start...
timeout /t 5

echo 🌐 Starting NGROK...
start "NGROK" cmd /k "ngrok http 5000"

echo.
echo ✅ Application started with NGROK!
echo 🌐 Check NGROK output for public URL
echo.
pause
```

### **7.2 Stop All Services**
```batch
@echo off
echo ========================================
echo   Stop Cloud Storage and NGROK
echo ========================================
echo.

echo 🛑 Stopping all services...
taskkill /f /im python.exe
taskkill /f /im ngrok.exe

echo ✅ All services stopped!
echo.
pause
```

---

## 🔧 **Langkah 8: Troubleshooting**

### **8.1 Common Issues**

#### **NGROK not found:**
```bash
# Check if NGROK is in PATH
ngrok version

# If not, use full path
C:\ngrok\ngrok.exe http 5000
```

#### **Port already in use:**
```bash
# Check what's using port 5000
netstat -ano | findstr :5000

# Kill process using port 5000
taskkill /f /pid PROCESS_ID
```

#### **Authentication failed:**
```bash
# Reconfigure authtoken
ngrok config add-authtoken YOUR_AUTHTOKEN_HERE
```

### **8.2 Debug Commands**
```bash
# Check NGROK status
ngrok status

# Check NGROK configuration
ngrok config check

# Test NGROK connection
ngrok http 5000 --log=stdout
```

---

## 📋 **Langkah 9: Security Considerations**

### **9.1 Free vs Paid NGROK**
- **Free:** Random subdomain, limited bandwidth
- **Paid:** Custom subdomain, more bandwidth, better performance

### **9.2 Security Best Practices**
- **Use HTTPS** - Always use HTTPS URL
- **Limit Access** - Don't share URL publicly
- **Monitor Usage** - Check NGROK web interface
- **Use Authentication** - Add basic auth if needed

---

## 🚀 **Langkah 10: Production Deployment**

### **10.1 NGROK for Testing Only**
- **Development** - Use NGROK for testing
- **Production** - Use proper hosting (Railway, Render, etc.)

### **10.2 Alternative Hosting**
- **Railway** - Free hosting dengan PostgreSQL
- **Render** - Free hosting dengan database
- **PythonAnywhere** - Free hosting untuk Python

---

## 📞 **Support & Help**

### **NGROK Documentation:**
- **NGROK Docs:** https://ngrok.com/docs
- **NGROK Dashboard:** https://dashboard.ngrok.com
- **NGROK Status:** https://status.ngrok.com

### **Flask Documentation:**
- **Flask Docs:** https://flask.palletsprojects.com/
- **Flask Deployment:** https://flask.palletsprojects.com/en/2.3.x/deploying/

---

## 🎉 **Success Checklist**

### **✅ Setup Checklist:**
- [ ] NGROK installed
- [ ] NGROK account created
- [ ] Authtoken configured
- [ ] Flask app running
- [ ] NGROK tunnel active
- [ ] Public URL accessible

### **✅ Testing Checklist:**
- [ ] Local access working
- [ ] Public URL working
- [ ] HTTPS URL working
- [ ] Mobile access working
- [ ] Different browser working

---

## 🔧 **Quick Commands**

### **Start Everything:**
```bash
# Start Flask
venv\Scripts\python.exe run.py

# Start NGROK (in new terminal)
ngrok http 5000
```

### **Stop Everything:**
```bash
# Stop Flask
Ctrl+C

# Stop NGROK
Ctrl+C
```

### **Check Status:**
```bash
# Check Flask
http://localhost:5000

# Check NGROK
http://127.0.0.1:4040
```

---

**NGROK setup complete! Your Cloud Storage app is now accessible from anywhere on the internet! 🌐✨**
