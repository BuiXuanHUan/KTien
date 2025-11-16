from flask import Flask, render_template, request, send_file, jsonify
import os
import sys
from werkzeug.utils import secure_filename
from translator import translate_file
import tempfile
import shutil

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['OUTPUT_FOLDER'] = 'outputs'
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB max file size

# Tạo thư mục nếu chưa tồn tại
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

ALLOWED_EXTENSIONS = {'srt', 'docx', 'doc', 'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    if 'file' not in request.files:
        return jsonify({'error': 'Không có file được upload'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Chưa chọn file'}), 400
    
    if not allowed_file(file.filename):
        return jsonify({'error': 'Định dạng file không được hỗ trợ. Chỉ chấp nhận: SRT, DOCX, DOC, PDF'}), 400
    
    try:
        # Lưu file tạm
        filename = secure_filename(file.filename)
        input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(input_path)
        
        # Dịch file
        output_path = translate_file(input_path, app.config['OUTPUT_FOLDER'])
        
        if output_path:
            return jsonify({
                'success': True,
                'download_url': f'/download/{os.path.basename(output_path)}',
                'filename': os.path.basename(output_path)
            })
        else:
            return jsonify({'error': 'Lỗi khi dịch file'}), 500
            
    except Exception as e:
        return jsonify({'error': f'Lỗi: {str(e)}'}), 500
    finally:
        # Xóa file input sau khi xử lý
        if os.path.exists(input_path):
            os.remove(input_path)

@app.route('/download/<filename>')
def download_file(filename):
    file_path = os.path.join(app.config['OUTPUT_FOLDER'], filename)
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return jsonify({'error': 'File không tồn tại'}), 404

if __name__ == '__main__':
    # Production: debug=False
    # Development: debug=True
    debug_mode = os.environ.get('FLASK_ENV') != 'production'
    app.run(debug=debug_mode, host='0.0.0.0', port=5000)

