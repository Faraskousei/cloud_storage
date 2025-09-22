# 🌥️ Cloud Storage dengan Authentication

Sistem cloud storage lengkap dengan authentication, role management, dan file isolation per tim. Dibangun menggunakan Flask, MySQL, dan interface web yang modern dan responsif.

## ✨ Fitur

### 🔐 **Authentication & Security**
- 👤 **User Management**: Sistem login/logout dengan session management
- 🏢 **3 Teams**: Development, Marketing, Operations dengan isolasi file
- 👑 **Role-Based Access**: Admin dan User dengan permission berbeda
- 🔒 **File Isolation**: File tiap tim tidak terlihat dengan tim lain
- 🛡️ **Security**: Password hashing, CSRF protection, input validation
- 📊 **Team Statistics**: Dashboard statistik per tim

### 🎨 **Interface Modern & Responsif**
- 📤 **Upload File**: Upload berbagai tipe file dengan drag & drop yang smooth
- 📥 **Download File**: Download file dengan animasi loading yang indah
- 👁️ **Preview File**: Preview file gambar dan text langsung di browser
- 🗑️ **Hapus File**: Hapus file dengan konfirmasi modal yang elegant
- 📊 **Statistik**: Dashboard statistik dengan animasi dan gradient yang menarik
- 📱 **Responsif**: Interface yang mobile-friendly dengan breakpoints yang optimal
- 🔒 **Validasi File**: Validasi tipe dan ukuran file dengan feedback visual
- ⚡ **Real-time**: Auto-refresh data setiap 30 detik dengan animasi smooth

### 🎭 **Animasi & Efek Visual**
- ✨ **Smooth Animations**: Transisi dan animasi yang smooth dengan cubic-bezier
- 🌈 **Gradient Design**: Gradient background dan button yang modern
- 🎯 **Hover Effects**: Efek hover yang responsif pada semua elemen
- 📱 **Mobile Optimized**: Touch-friendly interface untuk mobile
- 🎨 **Dark Mode Support**: Dukungan dark mode otomatis
- 🔄 **Loading States**: Loading spinner dan progress bar yang indah
- 📢 **Toast Notifications**: Notifikasi toast yang modern dan informatif

## 🎯 Tipe File yang Didukung

- **Dokumen**: txt, pdf, doc, docx, xls, xlsx, ppt, pptx
- **Gambar**: png, jpg, jpeg, gif
- **Arsip**: zip, rar
- **Media**: mp4, mp3, avi, mov

## 🚀 Cara Instalasi

### ⚡ Cara Cepat dengan Authentication (Windows)

**Untuk pengguna Windows, gunakan file batch yang sudah disediakan:**

1. **Setup XAMPP MySQL**
   - Pastikan XAMPP sudah diinstall dan MySQL service running
   - Import database: `mysql -u root -p < setup_database.sql`

2. **Double-click `setup_with_auth.bat`**
   - File ini akan otomatis install Python dependencies dan menjalankan aplikasi
   - Jika Python belum terinstall, akan ada instruksi untuk install Python

3. **Login dengan admin credentials:**
   - Username: `admin`
   - Password: `admin123`

### 🛠️ Cara Manual

#### 1. Persiapan Environment

```bash
# Clone atau download project ini
cd CLOUD_TEST

# Buat virtual environment (opsional tapi direkomendasikan)
python -m venv venv

# Aktifkan virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

#### 2. Install Dependencies

```bash
# Install semua package yang diperlukan
pip install -r requirements.txt
```

#### 3. Jalankan Aplikasi

```bash
# Cara 1: Menggunakan run.py (Direkomendasikan)
python run.py

# Cara 2: Langsung menggunakan app.py
python app.py
```

#### 4. Akses Aplikasi

Buka browser dan kunjungi: **http://localhost:5000**

### 📋 Persyaratan Sistem

- **Python 3.7+** ([Download di sini](https://www.python.org/downloads/))
- **XAMPP** dengan MySQL ([Download di sini](https://www.apachefriends.org/))
- **Windows 10/11** atau **Linux/Mac**
- **RAM minimal 512MB**
- **Storage minimal 100MB** (untuk file upload)

### 🔐 **Login Credentials**

#### **Admin Account**
- **Username**: `admin`
- **Password**: `admin123`
- **Team**: Development (Hijau)
- **Permissions**: Full access, dapat register user baru

#### **3 Teams Default**
- 🟢 **Development**: Tim pengembangan aplikasi
- 🟡 **Marketing**: Tim marketing dan promosi
- 🟣 **Operations**: Tim operasional dan support

## 📁 Struktur Project

```
CLOUD_TEST/
├── main.py                    # Aplikasi Flask utama dengan auth
├── models.py                  # Database models (User, Team, File)
├── auth.py                    # Authentication routes & logic
├── config.py                  # Konfigurasi aplikasi & database
├── setup_database.sql         # Database schema untuk MySQL
├── setup_with_auth.bat        # Setup script dengan authentication
├── requirements.txt           # Dependencies Python
├── uploads/                   # Folder penyimpanan file per team
│   ├── team_1/               # Development team files
│   ├── team_2/               # Marketing team files
│   └── team_3/               # Operations team files
├── templates/                 # Template HTML
│   ├── auth/                 # Authentication templates
│   │   ├── login.html        # Login page
│   │   ├── register.html     # Registration page
│   │   ├── profile.html      # User profile
│   │   └── change_password.html
│   ├── base.html             # Template dasar
│   ├── dashboard.html        # Dashboard utama
│   └── index.html            # Halaman redirect
└── static/                    # File statis (CSS, JS)
    ├── css/
    │   └── style.css         # Styling custom
    └── js/
        └── script.js         # JavaScript custom
```

## 🛠️ Konfigurasi

### Environment Variables

Anda dapat mengatur konfigurasi melalui environment variables:

```bash
# Set environment untuk production
set FLASK_ENV=production

# Set secret key untuk production (WAJIB!)
set SECRET_KEY=your-super-secret-key-here

# Set port custom
set PORT=8080
```

### Customisasi Konfigurasi

Edit file `config.py` untuk mengubah:

- **Ukuran maksimal file**: Ubah `MAX_CONTENT_LENGTH`
- **Tipe file yang diizinkan**: Edit `ALLOWED_EXTENSIONS`
- **Folder upload**: Ubah `UPLOAD_FOLDER`

## 🎨 Customisasi UI

### Mengubah Tema

Edit file `static/css/style.css` untuk mengubah:

- **Warna**: Ubah variabel warna CSS
- **Font**: Ganti font family
- **Layout**: Sesuaikan spacing dan sizing

### Menambah Fitur

Edit file `static/js/script.js` untuk menambah:

- **Keyboard shortcuts**: Tambah shortcut custom
- **Animasi**: Tambah efek visual
- **Validasi**: Tambah validasi custom

## 🔧 Pengembangan

### Menambah Fitur Baru

1. **Backend (Flask)**:
   - Tambah route baru di `app.py`
   - Tambah template HTML di folder `templates/`
   - Update konfigurasi di `config.py` jika perlu

2. **Frontend (HTML/CSS/JS)**:
   - Edit template di folder `templates/`
   - Tambah styling di `static/css/style.css`
   - Tambah interaksi di `static/js/script.js`

### Contoh: Menambah Fitur Rename File

```python
# Di app.py
@app.route('/rename/<filename>', methods=['POST'])
def rename_file(filename):
    new_name = request.form.get('new_name')
    # Logic rename file
    return redirect(url_for('index'))
```

## 🚀 Deployment

### Deploy ke Heroku

1. **Install Heroku CLI**
2. **Buat Procfile**:
   ```
   web: python run.py
   ```
3. **Deploy**:
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

### Deploy ke VPS

1. **Install dependencies di server**
2. **Set environment variables**
3. **Gunakan Gunicorn**:
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

## 🐛 Troubleshooting

### Error: Module not found
```bash
# Pastikan virtual environment aktif
venv\Scripts\activate

# Install ulang dependencies
pip install -r requirements.txt
```

### Error: Permission denied
```bash
# Pastikan folder uploads bisa diakses
chmod 755 uploads/
```

### Error: Port already in use
```bash
# Ganti port di run.py atau set environment variable
set PORT=8080
python run.py
```

### File tidak bisa diupload
- Periksa ukuran file (maksimal 100MB)
- Pastikan tipe file didukung
- Periksa permission folder uploads

## 📝 Changelog

### v1.0.0 (Current)
- ✅ Upload dan download file
- ✅ Preview file gambar dan text
- ✅ Hapus file
- ✅ Interface responsif
- ✅ Validasi file
- ✅ Statistik storage
- ✅ Auto-refresh

### Roadmap
- 🔄 User authentication
- 📁 Folder management
- 🔍 Search file
- 📊 Advanced analytics
- 🔗 Share file dengan link
- 📱 Mobile app

## 🤝 Kontribusi

1. Fork project ini
2. Buat branch fitur baru (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

## 📄 Lisensi

Project ini menggunakan lisensi MIT. Lihat file `LICENSE` untuk detail.

## 👨‍💻 Author

Dibuat dengan ❤️ menggunakan Flask dan Bootstrap.

---

**Selamat menggunakan Cloud Storage Sederhana! 🎉**

Jika ada pertanyaan atau masalah, silakan buat issue di repository ini.
