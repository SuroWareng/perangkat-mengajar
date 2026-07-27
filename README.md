# Perangkat Mengajar

Program lengkap untuk membuat dan mengelola perangkat pembelajaran yang terdiri dari:

1. **Prota (Program Tahunan)** - Rencana pembelajaran tahunan
2. **Promes (Program Semester)** - Rencana pembelajaran semester
3. **Modul Ajar** - Materi pembelajaran dalam bentuk modul

## Struktur Folder

```
perangkat-mengajar/
├── prota/
│   ├── templates/
│   ├── data/
│   └── README.md
├── promes/
│   ├── templates/
│   ├── data/
│   └── README.md
├── modul-ajar/
│   ├── templates/
│   ├── contoh/
│   └── README.md
├── docs/
│   └── panduan.md
└── README.md
```

## Cara Penggunaan

1. Pilih folder sesuai kebutuhan (Prota, Promes, atau Modul Ajar)
2. Gunakan template yang tersedia
3. Isi dengan data dan konten pembelajaran Anda
4. Simpan dalam folder `data/` atau `contoh/`

## Persyaratan

- Python 3.7+
- openpyxl (untuk Excel)
- Markdown support

## Instalasi

```bash
pip install -r requirements.txt
```

## Lisensi

MIT License
