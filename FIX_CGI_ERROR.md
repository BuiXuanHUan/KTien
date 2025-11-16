# 🔧 Fix Lỗi ModuleNotFoundError: No module named 'cgi'

## Vấn Đề

Lỗi này xảy ra khi Render sử dụng Python 3.12+ (module `cgi` đã bị removed).

## Giải Pháp

### 1. Đảm bảo dùng Python 3.11

Đã tạo file `runtime.txt` với nội dung:
```
python-3.11.9
```

### 2. Cập nhật render.yaml

Đã cập nhật `PYTHON_VERSION` thành `3.11.9`

### 3. Nếu vẫn lỗi, thử các bước sau:

#### Cách 1: Chỉ định Python version trong Render Dashboard

1. Vào Render Dashboard
2. Chọn Web Service của bạn
3. Vào tab "Settings"
4. Tìm "Python Version" hoặc "Environment"
5. Chọn Python 3.11 (không phải 3.12+)
6. Save và Redeploy

#### Cách 2: Thêm file runtime.txt vào repository

File `runtime.txt` đã được tạo với nội dung:
```
python-3.11.9
```

Đảm bảo file này được commit và push lên GitHub.

#### Cách 3: Cập nhật Build Command

Trong Render Dashboard, thay đổi Build Command thành:
```bash
pip install --upgrade pip && pip install -r requirements.txt
```

### 4. Nếu vẫn không được, thử downgrade dependencies

Có thể một dependency đang cố import `cgi`. Thử cập nhật `requirements.txt`:

```txt
Flask==3.0.0
googletrans==4.0.0rc1
python-docx==1.1.0
PyPDF2==3.0.1
pdfplumber==0.10.3
Werkzeug==3.0.1
python-multipart==0.0.6
gunicorn==21.2.0
httpcore==0.18.0
httpx==0.24.1
```

## Các Bước Thực Hiện

1. ✅ Đã tạo file `runtime.txt`
2. ✅ Đã cập nhật `render.yaml`
3. ✅ Đã cập nhật `requirements.txt`
4. 🔄 Commit và push lên GitHub
5. 🔄 Redeploy trên Render

## Kiểm Tra

Sau khi redeploy, kiểm tra:
- Build logs trong Render Dashboard
- Đảm bảo Python version là 3.11.x (không phải 3.12+)
- Xem error logs nếu vẫn còn lỗi

