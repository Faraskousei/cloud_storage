// Enhanced JavaScript untuk Cloud Storage
document.addEventListener('DOMContentLoaded', function() {
    // Inisialisasi tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Smooth scroll untuk semua link anchor
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Intersection Observer untuk animasi fade-in
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Observe semua elemen dengan class fade-in
    document.querySelectorAll('.fade-in').forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });

    // Enhanced file upload dengan drag & drop
    const fileInput = document.getElementById('file');
    const uploadArea = document.getElementById('uploadArea');
    const uploadForm = document.getElementById('uploadForm');
    
    if (fileInput && uploadArea) {
        // Drag & Drop functionality
        uploadArea.addEventListener('dragover', function(e) {
            e.preventDefault();
            e.stopPropagation();
            this.classList.add('drag-over');
        });

        uploadArea.addEventListener('dragleave', function(e) {
            e.preventDefault();
            e.stopPropagation();
            this.classList.remove('drag-over');
        });

        uploadArea.addEventListener('drop', function(e) {
            e.preventDefault();
            e.stopPropagation();
            this.classList.remove('drag-over');
            
            const files = e.dataTransfer.files;
            if (files.length > 0) {
                fileInput.files = files;
                handleFileSelect(files[0]);
            }
        });

        // Click to select file
        uploadArea.addEventListener('click', function() {
            fileInput.click();
        });

        fileInput.addEventListener('change', function(e) {
            if (e.target.files.length > 0) {
                handleFileSelect(e.target.files[0]);
            }
        });

        // Form submission dengan progress
        if (uploadForm) {
            uploadForm.addEventListener('submit', function(e) {
                const file = fileInput.files[0];
                if (!file) {
                    e.preventDefault();
                    showNotification('Pilih file terlebih dahulu', 'error');
                    return;
                }

                // Simulate upload progress
                showUploadProgress();
            });
        }
    }

    function handleFileSelect(file) {
        // Validasi ukuran file (100MB)
        const maxSize = 100 * 1024 * 1024; // 100MB
        if (file.size > maxSize) {
            showNotification('Ukuran file terlalu besar. Maksimal 100MB.', 'error');
            fileInput.value = '';
            return;
        }
        
        // Validasi tipe file
        const allowedTypes = ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'zip', 'rar', 'mp4', 'mp3'];
        const fileExtension = file.name.split('.').pop().toLowerCase();
        
        if (!allowedTypes.includes(fileExtension)) {
            showNotification('Tipe file tidak diizinkan. Tipe yang diizinkan: ' + allowedTypes.join(', '), 'error');
            fileInput.value = '';
            return;
        }
        
        // Update upload area dengan file info
        updateUploadArea(file);
        showNotification(`File "${file.name}" siap untuk diupload`, 'success');
    }

    function updateUploadArea(file) {
        const uploadArea = document.getElementById('uploadArea');
        const fileIcon = getFileIcon(file.name.split('.').pop().toLowerCase());
        
        uploadArea.innerHTML = `
            <div class="text-center py-4">
                <i class="${fileIcon} fa-3x mb-3"></i>
                <h5>${file.name}</h5>
                <p class="text-muted">${formatFileSize(file.size)} • Siap untuk upload</p>
            </div>
        `;
    }

    function getFileIcon(extension) {
        const iconMap = {
            'pdf': 'fas fa-file-pdf text-danger',
            'txt': 'fas fa-file-alt text-info',
            'jpg': 'fas fa-file-image text-success',
            'jpeg': 'fas fa-file-image text-success',
            'png': 'fas fa-file-image text-success',
            'gif': 'fas fa-file-image text-success',
            'doc': 'fas fa-file-word text-primary',
            'docx': 'fas fa-file-word text-primary',
            'xls': 'fas fa-file-excel text-success',
            'xlsx': 'fas fa-file-excel text-success',
            'ppt': 'fas fa-file-powerpoint text-warning',
            'pptx': 'fas fa-file-powerpoint text-warning',
            'zip': 'fas fa-file-archive text-secondary',
            'rar': 'fas fa-file-archive text-secondary',
            'mp4': 'fas fa-file-video text-danger',
            'mp3': 'fas fa-file-audio text-success'
        };
        return iconMap[extension] || 'fas fa-file text-muted';
    }

    function showUploadProgress() {
        const progressContainer = document.getElementById('uploadProgress');
        const progressBar = document.getElementById('progressBar');
        const progressPercent = document.getElementById('progressPercent');
        const uploadBtn = document.getElementById('uploadBtn');

        progressContainer.style.display = 'block';
        uploadBtn.disabled = true;
        uploadBtn.innerHTML = '<i class="fas fa-spinner fa-spin me-1"></i>Uploading...';

        // Simulate progress
        let progress = 0;
        const interval = setInterval(() => {
            progress += Math.random() * 15;
            if (progress >= 100) {
                progress = 100;
                clearInterval(interval);
            }
            
            progressBar.style.width = progress + '%';
            progressPercent.textContent = Math.round(progress) + '%';
        }, 200);
    }

    // Enhanced notification system
    function showNotification(message, type = 'info') {
        const notification = document.createElement('div');
        notification.className = `alert alert-${type === 'error' ? 'danger' : type} alert-dismissible fade show notification-toast`;
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            z-index: 9999;
            min-width: 300px;
            animation: slideInRight 0.3s ease-out;
        `;
        
        const icon = type === 'success' ? 'check-circle' : type === 'error' ? 'exclamation-circle' : 'info-circle';
        notification.innerHTML = `
            <i class="fas fa-${icon} me-2"></i>${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        `;
        
        document.body.appendChild(notification);
        
        // Auto remove after 5 seconds
        setTimeout(() => {
            if (notification.parentNode) {
                notification.style.animation = 'slideOutRight 0.3s ease-in';
                setTimeout(() => {
                    if (notification.parentNode) {
                        notification.parentNode.removeChild(notification);
                    }
                }, 300);
            }
        }, 5000);
    }

    // Auto-hide alerts setelah 5 detik
    setTimeout(function() {
        const alerts = document.querySelectorAll('.alert:not(.notification-toast)');
        alerts.forEach(function(alert) {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        });
    }, 5000);

    // Drag and drop functionality
    const uploadModal = document.getElementById('uploadModal');
    if (uploadModal) {
        uploadModal.addEventListener('dragover', function(e) {
            e.preventDefault();
            e.stopPropagation();
            e.currentTarget.classList.add('drag-over');
        });

        uploadModal.addEventListener('dragleave', function(e) {
            e.preventDefault();
            e.stopPropagation();
            e.currentTarget.classList.remove('drag-over');
        });

        uploadModal.addEventListener('drop', function(e) {
            e.preventDefault();
            e.stopPropagation();
            e.currentTarget.classList.remove('drag-over');
            
            const files = e.dataTransfer.files;
            if (files.length > 0) {
                const fileInput = document.getElementById('file');
                fileInput.files = files;
                fileInput.dispatchEvent(new Event('change'));
            }
        });
    }

    // Keyboard shortcuts
    document.addEventListener('keydown', function(e) {
        // Ctrl+U untuk upload
        if (e.ctrlKey && e.key === 'u') {
            e.preventDefault();
            const uploadModal = new bootstrap.Modal(document.getElementById('uploadModal'));
            uploadModal.show();
        }
        
        // Escape untuk tutup modal
        if (e.key === 'Escape') {
            const modals = document.querySelectorAll('.modal.show');
            modals.forEach(function(modal) {
                const bsModal = bootstrap.Modal.getInstance(modal);
                if (bsModal) {
                    bsModal.hide();
                }
            });
        }
    });

    // Refresh data setiap 30 detik
    setInterval(function() {
        // Hanya refresh jika tidak ada modal yang terbuka
        const openModals = document.querySelectorAll('.modal.show');
        if (openModals.length === 0) {
            fetch('/api/files')
                .then(response => response.json())
                .then(data => {
                    // Update file count jika berubah
                    const currentCount = document.querySelectorAll('tbody tr').length;
                    if (data.length !== currentCount) {
                        location.reload();
                    }
                })
                .catch(error => console.log('Auto-refresh error:', error));
        }
    }, 30000);
});

// Fungsi untuk format ukuran file
function formatFileSize(bytes) {
    if (bytes === 0) return '0 Bytes';
    
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
}

// Fungsi untuk konfirmasi delete dengan sweet alert style
// Enhanced delete function dengan confirmation
function deleteFile(filename) {
    const modal = new bootstrap.Modal(document.getElementById('deleteModal'));
    document.getElementById('deleteFileName').textContent = filename;
    document.getElementById('deleteForm').action = `/delete/${filename}`;
    modal.show();
}

// Refresh files function
function refreshFiles() {
    const refreshBtn = document.querySelector('[onclick="refreshFiles()"]');
    const icon = refreshBtn.querySelector('i');
    
    // Add spinning animation
    icon.classList.add('fa-spin');
    refreshBtn.disabled = true;
    
    // Reload page after short delay
    setTimeout(() => {
        location.reload();
    }, 1000);
}

// Fungsi untuk copy link download
function copyDownloadLink(filename) {
    const downloadUrl = `${window.location.origin}/download/${filename}`;
    navigator.clipboard.writeText(downloadUrl).then(function() {
        // Tampilkan toast notification
        const toast = document.createElement('div');
        toast.className = 'toast-notification';
        toast.innerHTML = '<i class="fas fa-check"></i> Link download disalin!';
        toast.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: #28a745;
            color: white;
            padding: 10px 20px;
            border-radius: 5px;
            z-index: 9999;
            animation: slideInRight 0.3s ease;
        `;
        
        document.body.appendChild(toast);
        
        setTimeout(function() {
            toast.style.animation = 'slideOutRight 0.3s ease';
            setTimeout(function() {
                document.body.removeChild(toast);
            }, 300);
        }, 2000);
    }).catch(function(err) {
        console.error('Gagal menyalin link:', err);
        alert('Gagal menyalin link ke clipboard');
    });
}

// CSS untuk animasi toast
const style = document.createElement('style');
style.textContent = `
    @keyframes slideInRight {
        from { transform: translateX(100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes slideOutRight {
        from { transform: translateX(0); opacity: 1; }
        to { transform: translateX(100%); opacity: 0; }
    }
    
    .drag-over {
        background-color: rgba(0,123,255,0.1) !important;
        border: 2px dashed #007bff !important;
    }
`;
document.head.appendChild(style);
