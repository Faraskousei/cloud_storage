# 🔍 Check Railway Logs - Debug Internal Server Error

## 📋 How to Check Railway Logs

### 1. Railway Dashboard
1. **Go to Railway:** https://railway.app
2. **Select Project:** Choose your Cloud Storage project
3. **Logs Tab:** Click on "Logs" tab
4. **View Logs:** Check recent deployment logs

### 2. What to Look For

#### ✅ Success Indicators:
```
✅ Database initialized successfully
✅ wsgi_debug.py imported successfully
✅ Flask app object accessible
🎉 WSGI debug completed successfully!
```

#### ❌ Error Indicators:
```
❌ WSGI debug failed: [error message]
❌ Database initialization failed: [error message]
❌ Failed to initialize app
```

### 3. Common Issues & Solutions

#### Issue 1: Database Connection Error
```
❌ Database initialization failed: connection refused
```
**Solution:**
- Check DATABASE_URL environment variable
- Ensure PostgreSQL database is created
- Verify database credentials

#### Issue 2: Import Error
```
❌ WSGI debug failed: No module named 'models'
```
**Solution:**
- Check if all files are uploaded to Railway
- Verify requirements.txt includes all dependencies
- Check file structure

#### Issue 3: Configuration Error
```
❌ WSGI debug failed: Invalid configuration
```
**Solution:**
- Check FLASK_ENV environment variable
- Verify SECRET_KEY is set
- Check config.py syntax

### 4. Debug Commands

#### Check Environment Variables:
```bash
echo $DATABASE_URL
echo $FLASK_ENV
echo $SECRET_KEY
```

#### Test WSGI Import:
```python
python -c "import wsgi_debug; print('WSGI OK')"
```

#### Test Database Connection:
```python
python -c "from app import app; print(app.config['SQLALCHEMY_DATABASE_URI'])"
```

### 5. Railway Logs Analysis

#### Successful Deployment:
```
[INFO] Starting gunicorn 21.2.0
[INFO] Listening at: http://0.0.0.0:8080
[INFO] Using worker: sync
[INFO] Booting worker with pid: X
🔧 Starting debug WSGI...
✅ Database initialized successfully
🎉 WSGI debug completed successfully!
```

#### Failed Deployment:
```
[ERROR] Exception in worker process
[ERROR] Worker (pid:X) exited with code 3
[ERROR] Shutting down: Master
[ERROR] Reason: Worker failed to boot.
```

### 6. Troubleshooting Steps

#### Step 1: Check Logs
- Go to Railway Dashboard
- Click on "Logs" tab
- Look for error messages
- Note the specific error

#### Step 2: Check Environment Variables
- Go to "Variables" tab
- Ensure all required variables are set:
  - `FLASK_ENV=production`
  - `SECRET_KEY=your-secret-key`
  - `DATABASE_URL=postgresql://...`

#### Step 3: Check Database
- Ensure PostgreSQL database is created
- Check DATABASE_URL format
- Verify database is accessible

#### Step 4: Check Files
- Verify all files are uploaded
- Check requirements.txt
- Ensure wsgi_debug.py exists

### 7. Common Fixes

#### Fix 1: Missing Environment Variables
```bash
# Add to Railway Variables
FLASK_ENV=production
SECRET_KEY=your-very-secret-key-here
```

#### Fix 2: Database Issues
```bash
# Check DATABASE_URL format
postgresql://user:pass@host:port/dbname
```

#### Fix 3: Import Issues
```bash
# Check if all files exist
ls -la
# Check requirements.txt
cat requirements.txt
```

### 8. Support Resources

#### Railway Documentation:
- **Railway Docs:** https://docs.railway.app
- **Railway Discord:** Railway Community
- **Railway Support:** Railway Support

#### Flask Documentation:
- **Flask Docs:** https://flask.palletsprojects.com/
- **Flask Error Handling:** https://flask.palletsprojects.com/en/2.3.x/errorhandling/

#### Debugging Tools:
- **Railway CLI:** `railway logs`
- **Local Testing:** `python wsgi_debug.py`
- **Error Testing:** `python test_error_handling.py`

---

**Happy Debugging! 🔍🚀**
