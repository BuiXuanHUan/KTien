#!/bin/bash
# Build script để đảm bảo dùng Python 3.11

# Tạo virtual environment với Python 3.11
python3.11 -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

