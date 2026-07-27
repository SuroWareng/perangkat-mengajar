# 📚 PANDUAN LENGKAP INSTALASI PERANGKAT MENGAJAR
## Dari Awal hingga Siap Digunakan

---

## 🎯 Daftar Isi
1. [Persyaratan Sistem](#persyaratan-sistem)
2. [Step 1: Persiapan](#step-1-persiapan)
3. [Step 2: Install Python](#step-2-install-python)
4. [Step 3: Clone Repository](#step-3-clone-repository)
5. [Step 4: Install Dependencies](#step-4-install-dependencies)
6. [Step 5: Jalankan Aplikasi](#step-5-jalankan-aplikasi)
7. [Step 6: Akses & Gunakan](#step-6-akses--gunakan)
8. [Troubleshooting](#troubleshooting)

---

## ✅ Persyaratan Sistem

### Yang Perlu Dipersiapkan:
- ✅ Komputer/Laptop dengan Windows, Mac, atau Linux
- ✅ Koneksi internet (untuk download)
- ✅ Browser (Chrome, Firefox, Edge, Safari)
- ✅ Minimal 500 MB storage kosong
- ✅ Python 3.7 atau lebih baru (akan kita install)

---

## 📋 STEP 1: Persiapan

### Buat Folder Kerja

#### Windows:
1. Buka **File Explorer** atau **Windows Explorer**
2. Pergi ke folder `C:\Users\YourUsername\Documents`
3. **Klik kanan** → Pilih **New Folder**
4. Beri nama: `perangkat-mengajar`
5. Buka folder yang baru dibuat

#### Mac/Linux:
Buka **Terminal** dan jalankan:
```bash
mkdir ~/perangkat-mengajar
cd ~/perangkat-mengajar
```

---

## 🐍 STEP 2: Install Python

### Windows:

#### 2.1 Download Python
1. Buka browser → https://www.python.org/downloads/
2. Klik tombol besar **"Download Python 3.11"** (atau versi terbaru)
3. File `.exe` akan terdownload

#### 2.2 Install Python
1. **Double-click** file `python-3.11.x.exe` yang sudah didownload
2. **PENTING:** Centang ✅ "**Add Python 3.11 to PATH**"
3. Klik **"Install Now"**
4. Tunggu hingga selesai (± 2 menit)
5. Klik **"Close"**

#### 2.3 Verifikasi Instalasi
1. Buka **Command Prompt** (tekan `Win + R`, ketik `cmd`, Enter)
2. Ketik: `python --version`
3. Jika keluar `Python 3.11.x` → Berhasil ✅

**Screenshot Help:**
```
C:\Users\YourUsername> python --version
Python 3.11.7
```

---

### Mac:

#### 2.1 Install Python via Homebrew
1. Buka **Terminal** (Cmd + Space, ketik "Terminal")
2. Install Homebrew dulu (jika belum):
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
3. Tunggu selesai, lalu install Python:
```bash
brew install python3
```

#### 2.2 Verifikasi
```bash
python3 --version
```

---

### Linux (Ubuntu/Debian):

```bash
sudo apt update
sudo apt install python3 python3-pip
python3 --version
```

---

## 📥 STEP 3: Clone Repository

### Option A: Menggunakan Git (Recommended)

#### Windows:
1. Download Git dari https://git-scm.com/download/win
2. Install seperti biasa
3. Buka **Command Prompt**
4. Pergi ke folder yang dibuat tadi:
```cmd
cd C:\Users\YourUsername\Documents\perangkat-mengajar
```
5. Clone repository:
```cmd
git clone https://github.com/SuroWareng/perangkat-mengajar.git .
```

#### Mac/Linux:
```bash
cd ~/perangkat-mengajar
git clone https://github.com/SuroWareng/perangkat-mengajar.git .
```

### Option B: Download Manual (Jika Git Tidak Tersedia)

1. Buka https://github.com/SuroWareng/perangkat-mengajar
2. Klik tombol hijau **"<> Code"**
3. Pilih **"Download ZIP"**
4. Extract file ZIP ke folder `perangkat-mengajar`
5. Sekarang folder Anda akan berisi semua file project

---

## 📦 STEP 4: Install Dependencies

### Windows:

#### 4.1 Buka Command Prompt
- Tekan `Win + R`
- Ketik `cmd`
- Tekan Enter

#### 4.2 Pergi ke Folder Project
```cmd
cd C:\Users\YourUsername\Documents\perangkat-mengajar
```

#### 4.3 Install Dependencies
```cmd
pip install -r requirements.txt
```

**Output yang diharapkan:**
```
Collecting Flask==2.3.3
  Downloading Flask-2.3.3-py3-none-any.whl (101 kB)
Collecting Flask-CORS==4.0.0
  Downloading Flask_CORS-4.0.0-py3-none-any.whl (14 kB)
...
Successfully installed Flask-2.3.3 Flask-CORS-4.0.0 ...
```

**Tunggu hingga selesai (± 3-5 menit)**

---

### Mac/Linux:

```bash
cd ~/perangkat-mengajar
pip3 install -r requirements.txt
```

---

## 🚀 STEP 5: Jalankan Aplikasi

### Windows:

#### 5.1 Command Prompt Sudah Terbuka?
Jika sudah di folder `perangkat-mengajar`, lanjut ke 5.2

Jika belum, buka Command Prompt baru:
```cmd
cd C:\Users\YourUsername\Documents\perangkat-mengajar
```

#### 5.2 Jalankan Aplikasi
```cmd
python run.py
```

**Output yang akan terlihat:**
```
============================================================
  Aplikasi Perangkat Mengajar - Generator Otomatis
============================================================

📂 Folder data akan tersimpan di: data/
🌐 Buka browser di: http://localhost:5000

Tekan CTRL+C untuk menghentikan aplikasi
============================================================
```

#### 5.3 Jangan Tutup Command Prompt Ini!
⚠️ **PENTING:** Jangan tutup jendela Command Prompt ini selama menggunakan aplikasi!

---

### Mac/Linux:

```bash
cd ~/perangkat-mengajar
python3 run.py
```

---

## 🌐 STEP 6: Akses & Gunakan

### 6.1 Buka Browser
1. Buka browser favorit Anda (Chrome, Firefox, Edge, Safari)
2. Di address bar, ketik:
```
http://localhost:5000
```
3. Tekan Enter

### 6.2 Aplikasi Siap Digunakan!

Anda akan melihat:
```
┌─────────────────────────────────────────┐
│   📚 Pembuat Perangkat Mengajar        │
│  Buat Program Tahunan, Program Semester│
│      dan Modul Ajar dengan mudah       │
│                                         │
│  ┌─────────────────────────────────┐  │
│  │ • Prota  • Promes  • Modul Ajar │  │
│  └─────────────────────────────────┘  │
└─────────────────────────────────────────┘
```

---

## 📖 Membuat PROTA dalam 5 Menit

### Langkah 1: Pilih Tab "Prota"
```
Klik tab "Prota" yang ada di bagian atas form
```

### Langkah 2: Isi Data Sekolah
```
Form 1:
- Nama Sekolah: SMA Negeri 1 Jakarta
- Mata Pelajaran: Biologi
- Kelas: X IPA 1
- Tahun Ajaran: 2024/2025

Form 2:
- Nama Guru: Budi Santoso, S.Pd
- NIP: 1975050219990331003
- Alamat: Jl. Merdeka No. 10
- Kota: Jakarta
- Provinsi: DKI Jakarta
```

### Langkah 3: Isi Kompetensi Inti
```
KI-1: Menghayati dan mengamalkan ajaran agama...
KI-2: Menunjukkan perilaku jujur, disiplin...
KI-3: Memahami, menerapkan, dan menganalisis...
KI-4: Mengolah, menalar, dan menyaji...
```

### Langkah 4: Tambah Materi Pokok

**Klik tombol "+ Tambah Materi"**

```
Material 1:
- Semester: Semester 1
- Kompetensi Dasar: 3.1
- Materi Pokok: Sel dan Organelnya
- Alokasi Waktu: 8 jam

Material 2:
- Semester: Semester 1
- Kompetensi Dasar: 3.2
- Materi Pokok: Transpor Membran
- Alokasi Waktu: 6 jam

(Ulangi untuk semua KD)
```

### Langkah 5: Export

**Pilih format:**
- 📄 **Export Word** → Download file .docx (siap cetak)
- 📊 **Export Excel** → Download file .xlsx (bisa diedit)
- 💾 **Simpan Data** → Backup format JSON

---

## 📁 Struktur Folder Setelah Instalasi

```
C:\Users\YourUsername\Documents\perangkat-mengajar\
├── app.py                      (Main aplikasi Flask)
├── run.py                       (File untuk jalankan)
├── requirements.txt             (Daftar library Python)
├── APP-README.md               (Dokumentasi lengkap)
├── QUICK-START.md              (Panduan cepat)
├── INSTALL.md                  (File ini)
│
├── templates/
│   └── index.html             (Interface web)
│
├── static/
│   └── js/
│       └── app.js             (JavaScript)
│
├── data/                       (Folder menyimpan data - auto-generated)
│   ├── prota_20240115_143022.json
│   ├── promes_20240115_143523.json
│   └── modul_20240115_144001.json
│
├── prota/
│   ├── templates/
│   ├── data/
│   └── README.md
│
├── promes/
│   ├── templates/
│   ├── data/
│   └── README.md
│
└── modul-ajar/
    ├── templates/
    ├── contoh/
    └── README.md
```

---

## 🎯 Checklist Instalasi

- [ ] **Python terinstall** (`python --version` berfungsi)
- [ ] **Git terinstall** (opsional, untuk clone repo)
- [ ] **Repository sudah di-clone** ke folder lokal
- [ ] **Dependencies terinstall** (`pip install -r requirements.txt` selesai)
- [ ] **Aplikasi berjalan** (`python run.py` tanpa error)
- [ ] **Browser bisa akses** http://localhost:5000
- [ ] **Form Prota bisa diisi** dan export berhasil

---

## 🐛 Troubleshooting

### Problem 1: "Python is not recognized"

**Penyebab:** Python tidak ditambahkan ke PATH

**Solusi:**
1. Uninstall Python
2. Install ulang dan **pastikan centang ✅ "Add Python to PATH"**
3. Restart Command Prompt
4. Coba lagi `python --version`

---

### Problem 2: "pip: command not found"

**Penyebab:** pip tidak terinstall atau PATH salah

**Solusi Windows:**
```cmd
python -m pip install -r requirements.txt
```

**Solusi Mac/Linux:**
```bash
python3 -m pip install -r requirements.txt
```

---

### Problem 3: "ERROR: Could not find a version that satisfies the requirement"

**Penyebab:** Internet lambat atau mirror pip error

**Solusi:**
```cmd
pip install --upgrade pip
pip install -r requirements.txt --no-cache-dir
```

---

### Problem 4: "Address already in use: 127.0.0.1:5000"

**Penyebab:** Port 5000 sudah dipakai aplikasi lain

**Solusi 1:** Tutup aplikasi yang pakai port 5000

**Solusi 2:** Ubah port di `run.py`
```python
# Buka run.py dengan text editor
# Cari baris: app.run(debug=True, host='0.0.0.0', port=5000)
# Ubah port 5000 jadi 8000:
# app.run(debug=True, host='0.0.0.0', port=8000)

# Lalu akses: http://localhost:8000
```

---

### Problem 5: "Module 'app' has no attribute 'run'"

**Penyebab:** File `app.py` tidak sesuai atau ada error

**Solusi:**
1. Pastikan file `app.py` di folder utama
2. Buka `app.py`, periksa baris terakhir ada `if __name__ == '__main__':`
3. Coba jalankan `python app.py` langsung

---

### Problem 6: "ModuleNotFoundError: No module named 'flask'"

**Penyebab:** Dependencies belum diinstall

**Solusi:**
```cmd
pip install -r requirements.txt
```

Jika masih error:
```cmd
pip install Flask==2.3.3
pip install Flask-CORS==4.0.0
pip install python-docx==0.8.11
pip install openpyxl==3.10.10
```

---

### Problem 7: Browser menampilkan "ERR_CONNECTION_REFUSED"

**Penyebab:** Server tidak berjalan atau URL salah

**Solusi:**
1. Pastikan Command Prompt dengan aplikasi masih terbuka
2. Lihat di Command Prompt apakah ada error
3. Coba akses http://localhost:5000 (bukan http://localhost)
4. Jika tidak bisa, stop (Ctrl+C) dan jalankan ulang `python run.py`

---

### Problem 8: "Permission denied" saat install

**Penyebab:** Permission folder tidak sesuai

**Solusi Windows:**
- Jalankan Command Prompt sebagai Administrator
- Klik kanan cmd.exe → "Run as Administrator"

**Solusi Mac/Linux:**
```bash
sudo pip install -r requirements.txt
```

---

## ⚡ Tips & Trik

### 1. Jalankan Aplikasi di Background (Windows)

**Buat file `start.bat`:**
```batch
@echo off
start python run.py
start http://localhost:5000
echo Aplikasi terbuka di browser dalam 3 detik...
timeout /t 3
```

Sekarang cukup double-click `start.bat` untuk menjalankan aplikasi.

---

### 2. Jalankan Aplikasi di Background (Mac/Linux)

**Buat file `start.sh`:**
```bash
#!/bin/bash
cd ~/perangkat-mengajar
python3 run.py &
sleep 2
open http://localhost:5000
```

Jalankan:
```bash
chmod +x start.sh
./start.sh
```

---

### 3. Backup Data Anda

**Folder `data/` berisi semua file yang Anda buat:**
```
data/
├── prota_*.json
├── promes_*.json
└── modul_*.json
```

**Backup secara berkala:**
- Copy folder `data/` ke USB/Cloud
- Atau gunakan Google Drive/OneDrive

---

### 4. Update Aplikasi

Jika ada update:
```cmd
cd C:\Users\YourUsername\Documents\perangkat-mengajar
git pull origin main
```

---

## 📞 Bantuan Lebih Lanjut

Jika masih ada masalah:

1. **Cek dokumentasi:**
   - `APP-README.md` - Fitur & konfigurasi
   - `docs/panduan.md` - Cara membuat Prota, Promes, Modul

2. **Cek contoh:**
   - `modul-ajar/contoh/modul_ajar_contoh.md` - Contoh modul lengkap

3. **Debug mode:**
   ```cmd
   python app.py
   ```
   (Lihat error message di terminal)

---

## 🎉 Selamat!

Anda sudah berhasil install dan siap menggunakan **Aplikasi Perangkat Mengajar**!

**Lanjutkan dengan:**
1. ✅ Buat Prota untuk semua mata pelajaran
2. ✅ Buat Promes per semester
3. ✅ Buat Modul Ajar untuk setiap KD
4. ✅ Export dan print semua file
5. ✅ Backup data secara berkala

---

**Happy Teaching! 🎓**

*Dibuat dengan ❤️ untuk memudahkan guru Indonesia*
