"""
WSGI entry point for production deployment
Sử dụng file này khi deploy lên shared hosting hoặc VPS
"""
import sys
import os

# Thêm thư mục hiện tại vào Python path
sys.path.insert(0, os.path.dirname(__file__))

from app import app as application

if __name__ == "__main__":
    application.run()

