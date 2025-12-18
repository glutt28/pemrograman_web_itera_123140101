# 📚 Aplikasi API Manajemen Matakuliah

Aplikasi RESTful API untuk manajemen data matakuliah menggunakan **Pyramid Framework** dan **PostgreSQL**. Aplikasi ini menyediakan operasi CRUD (Create, Read, Update, Delete) lengkap dengan validasi dan error handling.

## 🚀 Quick Start

```bash
# 1. Setup virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# 2. Install dependencies
pip install -r requirements.txt
pip install -e .

# 3. Buat database
python create_database.py --password password_anda

# 4. Edit konfigurasi database di development.ini dan alembic.ini

# 5. Jalankan migrasi
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head

# 6. Jalankan server
pserve development.ini
```

Server akan berjalan di `http://localhost:6543`

## 📋 Daftar Isi

- [Fitur](#-fitur)
- [Teknologi yang Digunakan](#-teknologi-yang-digunakan)
- [Persyaratan Sistem](#-persyaratan-sistem)
- [Instalasi Lengkap](#-instalasi-lengkap)
- [Konfigurasi Database](#-konfigurasi-database)
- [API Endpoints](#-api-endpoints)
- [Testing](#-testing)
- [Struktur Proyek](#-struktur-proyek)
- [Troubleshooting](#-troubleshooting)

## ✨ Fitur

- ✅ **CRUD Lengkap**: Create, Read, Update, Delete untuk data matakuliah
- ✅ **Validasi Data**: Validasi field wajib, tipe data, dan constraint
- ✅ **Error Handling**: Response error yang informatif dengan status code yang tepat
- ✅ **CORS Support**: Mendukung Cross-Origin Resource Sharing
- ✅ **Database Migration**: Menggunakan Alembic untuk migrasi database
- ✅ **RESTful API**: Mengikuti standar REST API

## 🛠 Teknologi yang Digunakan

- **Pyramid Framework 2.0.2** - Web framework Python yang fleksibel
- **PostgreSQL** - Database relasional
- **SQLAlchemy 1.4.53** - ORM untuk Python
- **Alembic 1.13.1** - Database migration tool
- **Waitress** - WSGI server
- **psycopg2** - PostgreSQL adapter untuk Python

## 💻 Persyaratan Sistem

- Python 3.7 atau lebih tinggi
- PostgreSQL 12 atau lebih tinggi
- pip (Python package manager)

## 📦 Instalasi Lengkap

### 1. Clone Repository

```bash
git clone <repository-url>
cd Prak-Last-Mathew
```

### 2. Buat Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
pip install -e .
```

### 4. Konfigurasi Database

#### Opsi 1: Menggunakan Script Python (Recommended)

```bash
# Dengan parameter password
python create_database.py --password password_anda

# Mode interaktif
python create_database.py --interactive

# Atau edit password di create_database.py (baris 18) lalu jalankan:
python create_database.py
```

#### Opsi 2: Menggunakan psql

```bash
psql -U postgres
CREATE DATABASE matakuliah_db;
\q
```

#### Opsi 3: Menggunakan pgAdmin

1. Buka pgAdmin
2. Klik kanan "Databases" → "Create" → "Database"
3. Nama: `matakuliah_db`
4. Klik "Save"

### 5. Edit Konfigurasi Database

Edit file `development.ini`:
```ini
sqlalchemy.url = postgresql://username:password@localhost:5432/matakuliah_db
```

Edit file `alembic.ini` dengan konfigurasi yang sama:
```ini
sqlalchemy.url = postgresql://username:password@localhost:5432/matakuliah_db
```

### 6. Jalankan Migrasi Database

```bash
# Buat file migrasi
alembic revision --autogenerate -m "Initial migration"

# Jalankan migrasi
alembic upgrade head
```

### 7. (Opsional) Tambahkan Data Awal

```bash
python init_data.py
```

## 🎯 API Endpoints

### Base URL
```
http://localhost:6543/api
```

### 1. Get All Matakuliah

**GET** `/api/matakuliah`

Mendapatkan daftar semua matakuliah.

**Request:**
```bash
curl -X GET http://localhost:6543/api/matakuliah
```

**Response (200 OK):**
```json
{
  "matakuliahs": [
    {
      "id": 1,
      "kode_mk": "IF101",
      "nama_mk": "Algoritma dan Pemrograman",
      "sks": 3,
      "semester": 1
    }
  ]
}
```

---

### 2. Get Matakuliah by ID

**GET** `/api/matakuliah/{id}`

Mendapatkan detail satu matakuliah berdasarkan ID.

**Request:**
```bash
curl -X GET http://localhost:6543/api/matakuliah/1
```

**Response (200 OK):**
```json
{
  "id": 1,
  "kode_mk": "IF101",
  "nama_mk": "Algoritma dan Pemrograman",
  "sks": 3,
  "semester": 1
}
```

**Error Response (404 Not Found):**
```json
{
  "error": "Matakuliah tidak ditemukan"
}
```

---

### 3. Create Matakuliah

**POST** `/api/matakuliah`

Menambahkan matakuliah baru.

**Request:**
```bash
curl -X POST http://localhost:6543/api/matakuliah \
  -H "Content-Type: application/json" \
  -d '{
    "kode_mk": "IF101",
    "nama_mk": "Algoritma dan Pemrograman",
    "sks": 3,
    "semester": 1
  }'
```

**Response (201 Created):**
```json
{
  "id": 1,
  "kode_mk": "IF101",
  "nama_mk": "Algoritma dan Pemrograman",
  "sks": 3,
  "semester": 1
}
```

**Error Response (400 Bad Request):**
```json
{
  "error": "Field kode_mk harus diisi"
}
```

**Error Response (409 Conflict):**
```json
{
  "error": "Kode matakuliah sudah ada"
}
```

---

### 4. Update Matakuliah

**PUT** `/api/matakuliah/{id}`

Mengupdate data matakuliah berdasarkan ID.

**Request:**
```bash
curl -X PUT http://localhost:6543/api/matakuliah/1 \
  -H "Content-Type: application/json" \
  -d '{
    "nama_mk": "Algoritma dan Pemrograman Dasar",
    "sks": 4
  }'
```

**Response (200 OK):**
```json
{
  "id": 1,
  "kode_mk": "IF101",
  "nama_mk": "Algoritma dan Pemrograman Dasar",
  "sks": 4,
  "semester": 1
}
```

**Error Response (404 Not Found):**
```json
{
  "error": "Matakuliah tidak ditemukan"
}
```

---

### 5. Delete Matakuliah

**DELETE** `/api/matakuliah/{id}`

Menghapus matakuliah berdasarkan ID.

**Request:**
```bash
curl -X DELETE http://localhost:6543/api/matakuliah/1
```

**Response (200 OK):**
```json
{
  "message": "Matakuliah berhasil dihapus"
}
```

**Error Response (404 Not Found):**
```json
{
  "error": "Matakuliah tidak ditemukan"
}
```

---

## 🧪 Testing

### Menggunakan Script Testing

**Windows:**
```bash
test_api.bat
```

**Linux/Mac:**
```bash
chmod +x test_api.sh
./test_api.sh
```

### Manual Testing dengan curl

```bash
# 1. Get all matakuliah
curl -X GET http://localhost:6543/api/matakuliah

# 2. Create matakuliah
curl -X POST http://localhost:6543/api/matakuliah \
  -H "Content-Type: application/json" \
  -d '{"kode_mk": "IF101", "nama_mk": "Algoritma dan Pemrograman", "sks": 3, "semester": 1}'

# 3. Get by ID
curl -X GET http://localhost:6543/api/matakuliah/1

# 4. Update matakuliah
curl -X PUT http://localhost:6543/api/matakuliah/1 \
  -H "Content-Type: application/json" \
  -d '{"sks": 4}'

# 5. Delete matakuliah
curl -X DELETE http://localhost:6543/api/matakuliah/1
```

### Menambahkan Data Awal

```bash
# Menggunakan script
python init_data.py

# Atau manual dengan curl
curl -X POST http://localhost:6543/api/matakuliah \
  -H "Content-Type: application/json" \
  -d '{"kode_mk": "IF101", "nama_mk": "Algoritma dan Pemrograman", "sks": 3, "semester": 1}'
```

## 📁 Struktur Proyek

```
Prak-Last-Mathew/
├── alembic/                      # Database migrations
│   ├── versions/                 # Migration files
│   ├── env.py                    # Alembic configuration
│   └── script.py.mako            # Migration template
├── matakuliah_api/               # Main application package
│   ├── models/                   # Database models
│   │   ├── __init__.py
│   │   └── matakuliah.py         # Matakuliah model
│   ├── views/                    # View handlers
│   │   ├── __init__.py
│   │   ├── matakuliah.py        # CRUD views
│   │   └── cors.py              # CORS handler
│   ├── __init__.py              # Application factory
│   └── routes.py                # Route definitions
├── alembic.ini                  # Alembic configuration
├── development.ini               # Development configuration
├── requirements.txt              # Python dependencies
├── setup.py                     # Package setup
├── create_database.py           # Database creation script
├── init_data.py                 # Initial data script
├── test_api.bat                 # Testing script (Windows)
├── test_api.sh                  # Testing script (Linux/Mac)
└── README.md                    # This file
```

## 📊 Model Data

### Matakuliah

| Atribut | Tipe | Deskripsi | Constraint |
|---------|------|-----------|------------|
| `id` | Integer | Primary key | Auto increment |
| `kode_mk` | Text | Kode mata kuliah | Unique, Not null |
| `nama_mk` | Text | Nama mata kuliah | Not null |
| `sks` | Integer | Jumlah SKS | Not null |
| `semester` | Integer | Semester pengambilan | Not null |

## ✅ Validasi

Aplikasi melakukan validasi pada:
- **Required fields**: Semua field wajib diisi saat create
- **Data types**: SKS dan semester harus berupa integer
- **Unique constraint**: Kode matakuliah harus unik
- **Empty strings**: Kode dan nama matakuliah tidak boleh kosong

## 🚨 Error Handling

| Status Code | Deskripsi |
|-------------|-----------|
| 200 | Success |
| 201 | Created |
| 400 | Bad Request (data tidak valid) |
| 404 | Not Found (matakuliah tidak ditemukan) |
| 409 | Conflict (kode matakuliah duplikat) |
| 500 | Internal Server Error |

## 🔧 Troubleshooting

### Database Connection Error

**Masalah:** Tidak bisa connect ke database

**Solusi:**
1. Pastikan PostgreSQL service berjalan
2. Cek kredensial di `development.ini` dan `alembic.ini`
3. Pastikan database `matakuliah_db` sudah dibuat

**Windows - Cek service:**
```powershell
Get-Service postgresql*
```

### Migration Error

**Masalah:** Error saat menjalankan migrasi

**Solusi:**
```bash
# Reset migrasi (HATI-HATI: akan menghapus data)
alembic downgrade base
alembic upgrade head
```

### Port Already in Use

**Masalah:** Port 6543 sudah digunakan

**Solusi:**
Edit `development.ini`:
```ini
listen = 0.0.0.0:8080
```

### Module Not Found

**Masalah:** Error import module

**Solusi:**
```bash
pip install -r requirements.txt
pip install -e .
```

### Password Authentication Failed

**Masalah:** Error saat membuat database

**Solusi:**
1. Gunakan script `create_database.py` dengan password yang benar
2. Atau reset password PostgreSQL (lihat dokumentasi PostgreSQL)
3. Atau gunakan pgAdmin untuk membuat database

## 📝 Script yang Tersedia

| Script | Deskripsi |
|--------|-----------|
| `create_database.py` | Membuat database PostgreSQL secara otomatis |
| `init_data.py` | Menambahkan data awal matakuliah |
| `test_api.bat` / `test_api.sh` | Script untuk testing semua endpoint |

## 🚀 Menjalankan Server

```bash
pserve development.ini
```

Server akan berjalan di `http://localhost:6543`

Untuk development dengan auto-reload:
```bash
pserve development.ini --reload
```

## 📚 Referensi

- [Pyramid Documentation](https://docs.pylonsproject.org/projects/pyramid/en/latest/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/)

## 📄 Lisensi

Proyek ini dibuat untuk keperluan praktikum mata kuliah Pemrograman Web.

---

**Dibuat dengan ❤️ menggunakan Pyramid Framework**
