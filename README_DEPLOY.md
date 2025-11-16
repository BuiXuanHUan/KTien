# 🚀 Hướng Dẫn Deploy - Tóm Tắt

## ⚠️ Tình Huống Của Bạn

Hosting 123host.com chỉ có **File Manager** (HTML tĩnh), không hỗ trợ Python/Flask.

## ✅ Giải Pháp: Deploy Lên Cloud Miễn Phí

### 🎯 Lựa Chọn Tốt Nhất: **Render.com**

- ✅ Miễn phí hoàn toàn
- ✅ Dễ sử dụng, không cần SSH
- ✅ Tự động deploy từ GitHub
- ✅ Có SSL miễn phí
- ⚠️ App sẽ "sleep" sau 15 phút không dùng (lần đầu load chậm)

---

## 📋 Các Bước Thực Hiện

### 1️⃣ Upload Code Lên GitHub

**Cách dễ nhất:**
- Tải **GitHub Desktop**: https://desktop.github.com
- Đăng nhập/Đăng ký
- Tạo repository mới
- Upload code

**Xem chi tiết:** `CHUAN_BI_GITHUB.txt`

### 2️⃣ Deploy Lên Render

1. Vào https://render.com
2. Đăng ký bằng GitHub
3. Tạo Web Service mới
4. Chọn repository GitHub
5. Cấu hình:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn wsgi:application`
6. Deploy và lấy URL

**Xem chi tiết:** `HUONG_DAN_DEPLOY_CLOUD.txt`

---

## 📁 File Cần Đọc

1. **`CHUAN_BI_GITHUB.txt`** - Hướng dẫn upload code lên GitHub
2. **`HUONG_DAN_DEPLOY_CLOUD.txt`** - Hướng dẫn deploy lên cloud
3. **`DEPLOY_CLOUD_FREE.md`** - Hướng dẫn chi tiết (đầy đủ)

---

## 🎉 Kết Quả

Sau khi deploy, bạn sẽ có:
- ✅ URL công khai (ví dụ: `https://dich-thuat.onrender.com`)
- ✅ SSL miễn phí (HTTPS)
- ✅ Không cần quản lý server
- ✅ Hoàn toàn miễn phí

---

## 🆘 Cần Giúp Đỡ?

Nếu gặp vấn đề, kiểm tra:
1. Code đã upload đầy đủ lên GitHub chưa?
2. Build Command và Start Command đã đúng chưa?
3. Xem logs trong Render dashboard để biết lỗi cụ thể

---

**Chúc bạn deploy thành công! 🚀**

