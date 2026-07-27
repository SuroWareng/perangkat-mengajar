# Perangkat Mengajar - Aplikasi Web

Aplikasi web interaktif untuk membuat **Prota (Program Tahunan)**, **Promes (Program Semester)**, dan **Modul Ajar** dengan mudah dan cepat.

## 🎯 Fitur Utama

✅ **Generator Prota**
- Input identitas sekolah dan guru
- Tambah kompetensi dasar dan materi pokok
- Export ke format Word dan Excel
- Hitung alokasi waktu otomatis

✅ **Generator Promes**
- Distribusi pembelajaran per minggu
- Manajemen libur dan cadangan waktu
- Simpan data dalam format JSON

✅ **Generator Modul Ajar**
- Buat modul dengan struktur lengkap
- Edit tujuan, kegiatan, dan penilaian
- Export ke format Word
- Template LKPD built-in

✅ **Export Otomatis**
- Download Prota dalam format Word (.docx)
- Download Prota dalam format Excel (.xlsx)
- Download Modul Ajar dalam format Word (.docx)
- Format profesional siap cetak

## 📋 Persyaratan Sistem

- Python 3.7+
- pip (Package Manager)
- Browser modern (Chrome, Firefox, Edge, Safari)

## 🚀 Instalasi & Setup

### 1. Clone Repository
```bash
git clone https://github.com/SuroWareng/perangkat-mengajar.git
cd perangkat-mengajar
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Jalankan Aplikasi
```bash
python app.py
```

### 4. Buka di Browser
Akses aplikasi di: **http://localhost:5000**

## 📁 Struktur Project

```
perangkat-mengajar/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── README.md                   # Dokumentasi
│
├── templates/
│   └── index.html             # UI aplikasi web
│
├── static/
│   └── js/
│       └── app.js             # JavaScript untuk interaksi
│
├── data/                       # Folder untuk menyimpan JSON data
│   └── (auto-generated)
│
└── prota/
    ├── templates/
    ├── data/
    └── README.md
    
promes/
    ├── templates/
    ├── data/
    └── README.md
    
modul-ajar/
    ├── templates/
    ├── contoh/
    └── README.md
```

## 💻 Cara Penggunaan

### Membuat Program Tahunan (Prota)

1. **Buka tab "Prota"** di aplikasi
2. **Isi identitas sekolah:**
   - Nama sekolah, alamat, kota, provinsi
   - Data guru (nama, NIP)
   - Mata pelajaran dan kelas

3. **Isi kompetensi inti:**
   - KI-1 (Spiritual), KI-2 (Sosial), KI-3 (Pengetahuan), KI-4 (Keterampilan)

4. **Tambah materi pokok:**
   - Klik "Tambah Materi"
   - Isi semester, KD, nama materi, dan alokasi waktu
   - Ulangi untuk semua materi

5. **Export:**
   - Klik "Export Word" untuk download .docx
   - Klik "Export Excel" untuk download .xlsx
   - Klik "Simpan Data" untuk backup JSON

### Membuat Program Semester (Promes)

1. **Buka tab "Promes"**
2. **Isi identitas dan pilih semester**
3. **Tambah kompetensi dasar**
4. **Distribusikan per minggu:**
   - Pilih bulan, minggu
   - Masukkan KD dan alokasi waktu
   - Tandai libur/cadangan jika ada
5. **Simpan data**

### Membuat Modul Ajar

1. **Buka tab "Modul Ajar"**
2. **Isi informasi umum:**
   - Judul modul
   - Data penyusun, sekolah, kelas
   - Alokasi waktu dan KD

3. **Isi komponen inti:**
   - Tujuan pembelajaran
   - Pemahaman bermakna
   - Pertanyaan pemantik
   - Kegiatan pembelajaran
   - Penilaian (formatif & sumatif)
   - Refleksi peserta didik

4. **Tambah lampiran:**
   - LKPD / Lembar kerja
   - Sumber belajar

5. **Export atau simpan data**

## 📊 Format Export

### Prota Word
- Header profesional
- Identitas lengkap sekolah
- Tabel KD dan materi dengan border
- Tanda tangan kepala sekolah dan guru
- Siap cetak A4

### Prota Excel
- Format table dengan header berwarna
- Kolom dengan lebar optimal
- Data terstruktur rapi
- Bisa diedit lebih lanjut di Excel

### Modul Ajar Word
- Struktur lengkap sesuai standar
- Heading dan subheading terformat
- Tabel untuk lampiran
- Font dan ukuran konsisten
- Siap cetak dan dijilid

## 🔧 Konfigurasi

### Mengubah Port
Edit di `app.py` baris terakhir:
```python
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # Ubah port di sini
```

### Mengubah Folder Penyimpanan Data
Edit di `app.py` baris 12:
```python
DATA_FOLDER = 'data'  # Ubah nama folder di sini
```

## 📝 Contoh Data

Sistem menyediakan:
- ✓ Template Prota dalam Markdown
- ✓ Template Promes dalam Markdown
- ✓ Contoh Modul Ajar lengkap (Sosiologi)
- ✓ Panduan lengkap penggunaan

Lihat folder `prota/`, `promes/`, dan `modul-ajar/` untuk referensi.

## 🐛 Troubleshooting

### Error: "ModuleNotFoundError: No module named 'flask'"
**Solusi:** Install dependencies
```bash
pip install -r requirements.txt
```

### Error: "Port 5000 already in use"
**Solusi:** Ubah port di `app.py` atau tutup aplikasi lain yang pakai port 5000

### File tidak bisa download
**Solusi:** 
- Pastikan folder `data/` ada dan writable
- Cek permission folder
- Refresh browser

### Format export tidak rapi
**Solusi:**
- Gunakan file yang sudah didownload langsung (jangan copy-paste)
- Buka dengan Word atau Excel versi terbaru
- Atur margin jika perlu di aplikasi Word/Excel

## 📞 Support

Untuk pertanyaan atau masalah:
1. Cek dokumentasi di folder `docs/`
2. Lihat contoh di folder `modul-ajar/contoh/`
3. Baca template di masing-masing folder

## 📄 Lisensi

MIT License - Bebas digunakan dan dimodifikasi

## 👨‍💻 Developer

Dibuat dengan ❤️ untuk memudahkan guru dalam membuat perangkat pembelajaran

---

**Versi:** 1.0.0  
**Updated:** 2024  
**Status:** Production Ready ✅
