# Manajemen Perpustakaan - Maha Asik

Aplikasi desktop manajemen perpustakaan berbasis Python (Tkinter) dengan sistem login, peminjaman buku, dan pengelolaan data via CSV.

## Bagian Pengerjaan Saya

### Login Form (`LoginForm`)
- **Desain antarmuka login** - Frame login dengan background, logo, dan input field nama lengkap + nomor telepon
- **Placeholder dinamis** - Teks petunjuk di entry yang hilang saat di klik dan muncul kembali jika kosong
- **Validasi 3 tahap:**
  1. `verif1` - Memastikan form tidak kosong
  2. `verif2` - Memvalidasi format (nama harus huruf, telepon harus angka)
  3. `verif3` - Mencocokkan data dengan `Data Peminjam.csv`
- **Routing** - Mengarahkan ke halaman Admin (`admin`/`021`) atau Public Space (peminjam terdaftar)

## Fitur

### Login
- Validasi input nama lengkap (huruf) dan nomor telepon (angka)
- Verifikasi data peminjam dari file CSV
- Login admin (`admin` / `021`) dan user (peminjam) terpisah

### Admin Center
- **Daftar Buku** - Lihat, tambah, ubah, dan hapus data buku
- **Daftar Peminjam** - Lihat daftar peminjam dan statusnya
- **Cari Peminjam** - Cari data peminjam berdasarkan ID (12 digit)
- **Atur Tanggal Pengembalian** - Menggunakan kalender, dengan perhitungan denda otomatis (Rp5.000/hari)

### Public Space
- **Daftar Buku** - Lihat koleksi buku
- **Pinjam Buku** - Pinjam buku dengan pilih tanggal via kalender (14 hari masa pinjam)
- **Cari Buku** - Cari buku berdasarkan judul, pengarang, tahun, atau genre
- **Status Peminjam** - Lihat status peminjaman dan denda

## Persyaratan

- Python 3.x
- Modul: `tkinter`, `tkcalendar`, `Pillow (PIL)`, `csv`, `datetime`

## Instalasi

```bash
pip install tkcalendar Pillow
```

## Menjalankan

```bash
python yea.py
```

## Struktur Data

### Data Buku (`Data Buku_Fix.csv`)
`ID, Judul, Nama Pengarang, Tahun Terbit, Genre`

### Data Peminjam (`Data Peminjam.csv`)
`ID (No. Telepon), Nama Peminjam, Judul Buku, Tanggal Peminjaman, Tanggal Pengembalian, Status, Denda`

### Audit Log (`auditlog.csv`)
Menyimpan data buku yang dihapus.

## Teknologi

- **Python Tkinter** - GUI
- **CSV** - Penyimpanan data
- **Pillow** - Pemrosesan gambar
- **tkcalendar** - Widget kalender
