# 🎯 Demo Authentication System

## 🚀 **Cara Menjalankan Demo**

### **1. Setup Database**
```bash
# Pastikan XAMPP MySQL running
# Import database schema
mysql -u root -p < setup_database.sql
```

### **2. Run Application**
```bash
# Windows
double-click setup_with_auth.bat

# Manual
python main.py
```

### **3. Access Application**
- **URL**: http://localhost:5000
- **Auto-redirect**: ke login page jika belum login

## 🔐 **Demo Login Credentials**

### **Admin Account**
- **Username**: `admin`
- **Password**: `admin123`
- **Team**: Development (Hijau)
- **Permissions**: Full access

### **Test Users** (Register via Admin)
- **Team Development**: Development files only
- **Team Marketing**: Marketing files only  
- **Team Operations**: Operations files only

## 🎭 **Demo Scenarios**

### **Scenario 1: Admin Login**
```
1. Login dengan admin/admin123
2. Dashboard shows all files from all teams
3. Can register new users
4. Can see team statistics
5. Full system access
```

### **Scenario 2: User Login**
```
1. Register new user via admin
2. Login with new user credentials
3. Dashboard shows only team files
4. Cannot see other teams' files
5. Limited permissions
```

### **Scenario 3: File Isolation**
```
1. Upload file as Development user
2. File goes to uploads/team_1/
3. Marketing user cannot see it
4. Operations user cannot see it
5. Only Development team can access
```

## 🎨 **UI/UX Demo Features**

### **1. Login Page**
- ✅ Modern login form
- ✅ Demo credentials display
- ✅ Password visibility toggle
- ✅ Remember me checkbox
- ✅ Auto-fill demo credentials

### **2. Dashboard (Authenticated)**
- ✅ Welcome message dengan nama user
- ✅ Team badge dengan warna
- ✅ Admin indicators
- ✅ Team-specific file listing
- ✅ Statistics per team

### **3. Navigation**
- ✅ User dropdown menu
- ✅ Team color coding
- ✅ Role-based menu items
- ✅ Profile access
- ✅ Logout functionality

### **4. File Management**
- ✅ Team isolation display
- ✅ Owner information
- ✅ Team badges pada files
- ✅ Access control indicators

## 🔧 **Technical Demo**

### **1. Database Integration**
```sql
-- Show teams
SELECT * FROM teams;

-- Show users
SELECT username, email, full_name, is_admin, team_id FROM users;

-- Show files with team info
SELECT f.original_name, t.name as team, u.full_name as owner 
FROM files f 
JOIN teams t ON f.team_id = t.id 
JOIN users u ON f.owner_id = u.id;
```

### **2. File Structure**
```
uploads/
├── team_1/ (Development files)
├── team_2/ (Marketing files)
└── team_3/ (Operations files)
```

### **3. Session Management**
- ✅ User session tracking
- ✅ Team info in session
- ✅ Role permissions
- ✅ Auto-logout on session expiry

## 📊 **Demo Statistics**

### **Before Authentication**
- ❌ No user management
- ❌ No file isolation
- ❌ No role-based access
- ❌ All files visible to everyone

### **After Authentication**
- ✅ 3 Teams dengan isolasi
- ✅ Admin & User roles
- ✅ File isolation per team
- ✅ User management system
- ✅ Session management
- ✅ Security features

## 🎯 **Demo Checklist**

### **Authentication Features**
- [ ] Login dengan admin credentials
- [ ] Register new user sebagai admin
- [ ] Login dengan user baru
- [ ] Profile management
- [ ] Password change
- [ ] Logout functionality

### **Role-Based Access**
- [ ] Admin dapat lihat semua files
- [ ] User hanya lihat team files
- [ ] Admin dapat register user
- [ ] User tidak dapat register user
- [ ] Team isolation working

### **File Management**
- [ ] Upload file ke team folder
- [ ] Download file dengan access control
- [ ] Preview file dengan team check
- [ ] Delete file dengan permission check
- [ ] File listing dengan team info

### **UI/UX Features**
- [ ] Responsive login form
- [ ] Dashboard dengan team info
- [ ] Navigation dengan user dropdown
- [ ] Team color coding
- [ ] Role indicators

## 🔍 **Demo Testing**

### **1. Security Testing**
```bash
# Test access control
1. Login as Development user
2. Try to access Marketing files
3. Should get access denied

# Test admin access
1. Login as admin
2. Should see all files
3. Should be able to register users
```

### **2. File Isolation Testing**
```bash
# Test file upload
1. Upload file as Development user
2. Check file goes to team_1 folder
3. Login as Marketing user
4. Should not see Development file
```

### **3. Session Testing**
```bash
# Test session management
1. Login with remember me
2. Close browser
3. Reopen browser
4. Should still be logged in

# Test logout
1. Click logout
2. Should redirect to login
3. Should clear session
```

## 📱 **Mobile Demo**

### **Mobile Features**
- ✅ Touch-friendly login
- ✅ Responsive dashboard
- ✅ Mobile navigation
- ✅ Touch file management
- ✅ Mobile-optimized modals

### **Desktop Features**
- ✅ Full keyboard navigation
- ✅ Drag & drop upload
- ✅ Multi-window support
- ✅ Advanced file management

## 🎨 **Visual Demo**

### **Color Coding**
- 🟢 **Development**: Green (#10b981)
- 🟡 **Marketing**: Yellow (#f59e0b)
- 🟣 **Operations**: Purple (#8b5cf6)

### **Icons & Indicators**
- 👑 **Admin**: Crown icon
- 👤 **User**: User icon
- 🏷️ **Team**: Team badge dengan warna
- 📁 **Files**: File type icons

## 🚀 **Demo Tips**

### **Untuk Presentasi**
1. **Start dengan Admin**: Show full system access
2. **Register User**: Demonstrate user creation
3. **Switch User**: Show team isolation
4. **File Operations**: Show access control
5. **Mobile View**: Show responsive design

### **Untuk Testing**
1. **Test All Teams**: Login dengan setiap team
2. **Test File Upload**: Upload ke setiap team
3. **Test Access Control**: Try cross-team access
4. **Test Admin Features**: Full admin functionality
5. **Test Mobile**: Responsive behavior

## 📝 **Demo Notes**

### **Browser Compatibility**
- ✅ Chrome: Full support
- ✅ Firefox: Full support
- ✅ Safari: Full support
- ✅ Edge: Full support

### **Performance**
- ✅ Fast login/logout
- ✅ Efficient file loading
- ✅ Smooth animations
- ✅ Responsive UI

**Selamat mencoba demo authentication system! 🎉**
