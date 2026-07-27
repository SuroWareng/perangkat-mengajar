# Panduan Quick Start - Perangkat Mengajar

## ⚡ Quick Start (5 Menit)

### 1️⃣ Instalasi (2 menit)

```bash
# Clone repository
git clone https://github.com/SuroWareng/perangkat-mengajar.git
cd perangkat-mengajar

# Install dependencies
pip install -r requirements.txt

# Jalankan aplikasi
python run.py
```

### 2️⃣ Akses Aplikasi

Buka browser ke: **http://localhost:5000**

Anda akan melihat interface yang user-friendly dengan 3 tab:
- 📅 **Prota** - Program Tahunan
- 📅 **Promes** - Program Semester  
- 📚 **Modul Ajar** - Materi Pembelajaran

### 3️⃣ Buat Prota dalam 3 Langkah

**Langkah 1: Isi Data Sekolah**
- Nama sekolah, mata pelajaran, kelas
- Data guru (nama, NIP)
- Tahun ajaran

**Langkah 2: Isi Kompetensi Inti**
- KI-1, KI-2, KI-3, KI-4
- Bisa copy-paste dari kurikulum

**Langkah 3: Tambah Materi**
- Klik "+ Tambah Materi"
- Isi KD, materi, dan alokasi waktu
- Ulangi untuk semua KD

**Langkah 4: Export**
- Klik "Export Word" atau "Export Excel"
- File otomatis terdownload
- Siap cetak!

### 4️⃣ Tips Penggunaan

✅ **Prota:**
- Harus punya kurikulum/silabus dulu
- Alokasi waktu disesuaikan dengan kalender akademik
- Export ke Word/Excel untuk editing lebih lanjut

✅ **Promes:**
- Isi berdasarkan Prota yang sudah dibuat
- Distribusikan per minggu dalam semester
- Tambahkan libur, ulangan, dan cadangan

✅ **Modul Ajar:**
- Buat 1 modul per kompetensi dasar
- Isi kegiatan pembelajaran detail
- Export Word untuk diprint/dijilid

## 📦 Data Tersimpan Di Mana?

Semua data JSON otomatis tersimpan di folder: **`data/`**

Contoh:
- `prota_20240115_143022.json`
- `promes_20240115_143523.json`
- `modul_20240115_144001.json`

Anda bisa backup folder ini atau pindahkan ke tempat lain.

## 🎨 Customization

### Ubah Warna (Opsional)
Edit `templates/index.html` cari bagian `<style>` dan ubah:
```css
/* Ubah dari ungu ke biru */
background: linear-gradient(135deg, #0066ff 0%, #0044cc 100%);
```

### Ubah Port
Edit `run.py` atau `app.py` baris terakhir:
```python
app.run(debug=True, host='0.0.0.0', port=8000)  # Ganti 5000 jadi 8000
```

## 🔗 File Berguna

- 📖 **APP-README.md** - Dokumentasi lengkap
- 📋 **docs/panduan.md** - Panduan membuat Prota, Promes, Modul
- 📄 **prota/templates/prota_template.md** - Contoh Prota
- 📄 **modul-ajar/contoh/modul_ajar_contoh.md** - Contoh Modul Ajar

## ⚙️ Troubleshooting

| Problem | Solusi |
|---------|--------|
| Port 5000 sudah terpakai | Ubah port di run.py |
| Module not found | `pip install -r requirements.txt` |
| File tidak bisa download | Buat folder `data/` manual |
| Aplikasi error | Cek console Python untuk error message |

## 🎓 Next Steps

1. ✅ Buat Prota untuk semua mata pelajaran
2. ✅ Buat Promes per semester
3. ✅ Buat Modul Ajar untuk setiap KD
4. ✅ Export dan print semua file
5. ✅ Backup data JSON ke cloud

---

**Happy Teaching! 🎉**
