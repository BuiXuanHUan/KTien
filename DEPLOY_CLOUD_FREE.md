# 🚀 Deploy Lên Cloud Miễn Phí (Không Cần SSH/Terminal)

Vì hosting của bạn chỉ hỗ trợ HTML tĩnh, chúng ta sẽ deploy lên **cloud service miễn phí** hỗ trợ Python/Flask.

## 🌟 Các Lựa Chọn Tốt Nhất (Miễn Phí)

### 1. **Render.com** ⭐ (Khuyến nghị - Dễ nhất)
- ✅ Miễn phí
- ✅ Tự động deploy từ GitHub
- ✅ Hỗ trợ Python/Flask
- ✅ Có SSL miễn phí
- ✅ Không cần SSH

### 2. **Railway.app**
- ✅ Miễn phí (có giới hạn)
- ✅ Deploy nhanh
- ✅ Hỗ trợ Python

### 3. **Fly.io**
- ✅ Miễn phí
- ✅ Tốc độ nhanh
- ⚠️ Hơi phức tạp hơn

---

## 📋 HƯỚNG DẪN DEPLOY LÊN RENDER.COM (Dễ Nhất)

### Bước 1: Tạo Tài Khoản GitHub (Nếu chưa có)

1. Truy cập: https://github.com
2. Đăng ký tài khoản miễn phí
3. Tạo repository mới (ví dụ: `dich-thuat-tool`)

### Bước 2: Upload Code Lên GitHub

**Cách A: Qua GitHub Desktop (Dễ nhất)**
1. Tải GitHub Desktop: https://desktop.github.com
2. Cài đặt và đăng nhập
3. File → Add Local Repository
4. Chọn thư mục `E:\TOOL`
5. Commit và Push lên GitHub

**Cách B: Qua Web (Upload trực tiếp)**
1. Tạo repository mới trên GitHub
2. Click "uploading an existing file"
3. Kéo thả tất cả file (trừ `venv`, `__pycache__`, `uploads`, `outputs`)
4. Commit

### Bước 3: Tạo Tài Khoản Render

1. Truy cập: https://render.com
2. Đăng ký bằng GitHub (dễ nhất)
3. Xác nhận email

### Bước 4: Deploy Trên Render

1. **Tạo Web Service mới:**
   - Click "New +" → "Web Service"
   - Chọn repository GitHub của bạn
   - Click "Connect"

2. **Cấu hình:**
   - **Name**: `dich-thuat` (hoặc tên bạn muốn)
   - **Region**: Singapore (gần Việt Nam nhất)
   - **Branch**: `main` hoặc `master`
   - **Root Directory**: (để trống)
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn wsgi:application`

3. **Advanced Settings:**
   - Click "Advanced"
   - **Environment Variables**: (không cần thêm gì)
   - **Plan**: Chọn **Free**

4. **Click "Create Web Service"**

5. **Chờ deploy** (5-10 phút)

6. **Lấy URL**: Render sẽ cung cấp URL dạng: `https://dich-thuat.onrender.com`

### Bước 5: Kiểm Tra

1. Truy cập URL được cung cấp
2. Test upload và dịch file
3. ✅ Xong!

---

## 📋 HƯỚNG DẪN DEPLOY LÊN RAILWAY.APP

### Bước 1: Tạo Tài Khoản

1. Truy cập: https://railway.app
2. Đăng ký bằng GitHub
3. Xác nhận email

### Bước 2: Deploy

1. Click "New Project"
2. Chọn "Deploy from GitHub repo"
3. Chọn repository của bạn
4. Railway sẽ tự động detect Python và deploy
5. Chờ deploy xong
6. Click "Generate Domain" để lấy URL

### Bước 3: Cấu Hình (Nếu cần)

1. Vào Settings → Variables
2. Thêm biến môi trường (nếu cần)
3. Vào Deployments → Redeploy

---

## 🔧 Tạo File Cấu Hình Cho Render

Tôi sẽ tạo file `render.yaml` để tự động cấu hình:

```yaml
services:
  - type: web
    name: dich-thuat
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn wsgi:application
    envVars:
      - key: PYTHON_VERSION
        value: 3.11.0
```

---

## 📝 Lưu Ý Quan Trọng

### 1. File Cần Upload Lên GitHub

✅ **Cần upload:**
- app.py
- translator.py
- wsgi.py
- requirements.txt
- templates/index.html
- gunicorn_config.py
- .gitignore
- README.md

❌ **KHÔNG upload:**
- venv/
- __pycache__/
- uploads/
- outputs/
- *.pyc

### 2. Giới Hạn Free Tier

**Render:**
- ⚠️ App sẽ "sleep" sau 15 phút không dùng (lần đầu load sẽ chậm)
- ✅ Có thể upgrade để không sleep ($7/tháng)

**Railway:**
- ⚠️ Có giới hạn $5 credit/tháng (đủ dùng cho app nhỏ)
- ✅ Tự động scale

### 3. Tối Ưu Cho Free Tier

- Giảm timeout trong code
- Tối ưu kích thước file upload
- Cache kết quả nếu có thể

---

## 🐛 Xử Lý Lỗi

### Lỗi: "Build failed"

1. Kiểm tra `requirements.txt` có đúng không
2. Kiểm tra Python version trong Render settings
3. Xem build logs để biết lỗi cụ thể

### Lỗi: "Application error"

1. Kiểm tra Start Command: `gunicorn wsgi:application`
2. Kiểm tra file `wsgi.py` có tồn tại không
3. Xem logs trong Render dashboard

### Lỗi: "Module not found"

1. Kiểm tra `requirements.txt` có đầy đủ không
2. Thử rebuild lại

---

## ✅ Checklist Deploy

- [ ] Code đã upload lên GitHub
- [ ] Tạo tài khoản Render/Railway
- [ ] Tạo Web Service mới
- [ ] Cấu hình Build Command và Start Command
- [ ] Deploy thành công
- [ ] Test ứng dụng hoạt động
- [ ] Lưu URL để sử dụng

---

## 🎉 Kết Quả

Sau khi deploy, bạn sẽ có:
- ✅ URL công khai để truy cập (ví dụ: `https://dich-thuat.onrender.com`)
- ✅ SSL miễn phí (HTTPS)
- ✅ Tự động deploy khi push code mới lên GitHub
- ✅ Không cần quản lý server

**Chúc bạn deploy thành công! 🚀**

