# Aplikasi Jadwal Kuliah

Aplikasi web sederhana untuk mengelola jadwal kuliah.

## Fitur Aplikasi

- Tambah jadwal kuliah baru
- Edit jadwal yang sudah ada
- Hapus jadwal
- Penyimpanan lokal menggunakan localStorage
- Tampilan waktu real-time
- Antarmuka yang responsif dan user-friendly

## Screenshot

![Screenshot Aplikasi](screenshot.png)

## Implementasi Fitur ES6+

1. **Class Declaration**
   - Penggunaan class `JadwalItem` untuk membuat object jadwal

2. **Arrow Functions**
   - Implementasi pada berbagai fungsi seperti `updateWaktuSekarang`, `simpanKeStorage`, dll.

3. **Template Literals**
   - Digunakan untuk membuat string HTML dalam fungsi `renderJadwal`
   - Format tampilan waktu dalam `updateWaktuSekarang`

4. **Destructuring & Default Parameters**
   - Penggunaan dalam constructor class `JadwalItem`

5. **Async/Await**
   - Implementasi pada fungsi `updateWaktuSekarang` untuk simulasi delay

6. **Local Storage API**
   - Penyimpanan data menggunakan `localStorage.setItem` dan `localStorage.getItem`

7. **Array Methods**
   - Penggunaan `map`, `forEach`, dan `splice` untuk manipulasi array

8. **String Methods**
   - Penggunaan `padStart` untuk format waktu
   - Method `trim()` untuk pembersihan input


