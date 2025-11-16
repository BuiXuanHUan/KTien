# 🌐 Tool Dịch Thuật - SRT, Word, PDF

Tool dịch thuật tự động từ tiếng Anh sang tiếng Việt cho các file:
- **SRT** (phụ đề video)
- **Word** (.docx, .doc)
- **PDF** (sẽ chuyển đổi sang Word sau khi dịch)

## ✨ Tính năng

- ✅ Dịch file SRT giữ nguyên format và timestamp
- ✅ Dịch file Word giữ nguyên định dạng
- ✅ Dịch file PDF và chuyển đổi sang Word
- ✅ Web interface đẹp mắt, dễ sử dụng
- ✅ Hỗ trợ drag & drop
- ✅ Tự động download file đã dịch

## 🚀 Cài đặt

### 1. Cài đặt Python dependencies

```bash
pip install -r requirements.txt
```

### 2. Chạy ứng dụng

```bash
python app.py
```

### 3. Mở trình duyệt

Truy cập: `http://localhost:5000`

## 📖 Hướng dẫn sử dụng

1. **Upload file**: Kéo thả file vào vùng upload hoặc click để chọn file
2. **Chọn file**: Chọn file SRT, DOCX, DOC hoặc PDF cần dịch
3. **Dịch**: Click nút "🚀 Dịch File"
4. **Download**: Sau khi dịch xong, click "⬇️ Tải file đã dịch"

## 📁 Cấu trúc Project

```
TOOL/
├── app.py              # Flask backend
├── translator.py       # Module xử lý dịch thuật
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html     # Frontend web interface
├── uploads/           # Thư mục lưu file upload (tự động tạo)
└── outputs/           # Thư mục lưu file đã dịch (tự động tạo)
```

## 🔧 Cấu hình

- **Port mặc định**: 5000
- **Kích thước file tối đa**: 50MB
- **Định dạng hỗ trợ**: .srt, .docx, .doc, .pdf

## 📝 Lưu ý

- File PDF sau khi dịch sẽ được chuyển đổi sang định dạng Word (.docx)
- File SRT sẽ giữ nguyên format và timestamp, chỉ dịch nội dung text
- Tool sử dụng Google Translate API (googletrans) để dịch thuật
- File upload sẽ tự động xóa sau khi xử lý xong

## 🐛 Xử lý lỗi

Nếu gặp lỗi với googletrans, có thể cần cài đặt phiên bản cụ thể:

```bash
pip install googletrans==4.0.0rc1
```

Hoặc sử dụng thư viện khác như `deep-translator`:

```bash
pip install deep-translator
```

## 📄 License

MIT License

