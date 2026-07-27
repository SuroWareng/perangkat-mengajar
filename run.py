#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script untuk menjalankan aplikasi Perangkat Mengajar
Pastikan sudah install requirements.txt terlebih dahulu
"""

import sys
import os
from app import app

if __name__ == '__main__':
    print("="*60)
    print("  Aplikasi Perangkat Mengajar - Generator Otomatis")
    print("="*60)
    print()
    print("📂 Folder data akan tersimpan di: data/")
    print("🌐 Buka browser di: http://localhost:5000")
    print()
    print("Tekan CTRL+C untuk menghentikan aplikasi")
    print("="*60)
    print()
    
    try:
        app.run(debug=True, host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("\n\nAplikasi dihentikan.")
        sys.exit(0)
