# Program Nilai Mahasiswa

Proyek ini berisi program Python sederhana (`nilai_mahasiswa.py`) untuk mengelola data nilai mahasiswa dan menampilkan informasi seperti nilai akhir, grade, data tertinggi/terendah, filter berdasarkan grade, serta rata-rata kelas.

## Ringkasan

- Nama file utama: `nilai_mahasiswa.py`
- Bahasa: Python 

Program menyediakan menu interaktif (console) dengan opsi untuk melihat data, menambah data, mencari nilai tertinggi/terendah, memfilter berdasarkan grade, menghitung rata-rata kelas, dan keluar.

## Penjelasan fungsi (detail)

Semua penjelasan di bawah merujuk pada fungsi yang ada di `nilai_mahasiswa.py`.

1. `hitung_nilai_akhir(mhs: Mahasiswa) -> float`
   - Deskripsi: Menghitung nilai akhir seorang mahasiswa berdasarkan bobot: 30% UTS, 40% UAS, 30% Tugas.
   - Input: `mhs` — dict yang mengandung kunci `nilai_uts`, `nilai_uas`, `nilai_tugas` (angka/int/float).
   - Output: `float` — nilai akhir, dibulatkan ke 2 desimal.
   - Catatan: Fungsi meng-cast nilai ke `float` sebelum perhitungan. Jika kunci tidak ada atau bukan angka, akan memunculkan exception.

2. `tentukan_grade(nilai_akhir: float) -> str`
   - Deskripsi: Menentukan grade huruf (A/B/C/D/E) berdasarkan `nilai_akhir`.
   - Aturan: >=80 => A, >=70 => B, >=60 => C, >=50 => D, <50 => E.
   - Input: `nilai_akhir` — float.
   - Output: `str` — satu huruf grade.

3. `tampilkan_tabel(data: List[Mahasiswa]) -> None`
   - Deskripsi: Menampilkan list mahasiswa dalam format tabel di console. Menampilkan kolom: No, Nama, NIM, UTS, UAS, Tugas, Akhir, Grade.
   - Input: `data` — list of dict.
   - Output: Teks tabel ke stdout (console).
   - Catatan: Fungsi menggunakan helper `_format_row` untuk perataan kolom.

4. `cari_tertinggi_terendah(data: List[Mahasiswa]) -> Tuple[Mahasiswa, Mahasiswa]`
   - Deskripsi: Mencari mahasiswa dengan nilai akhir tertinggi dan terendah.
   - Input: `data` — list mahasiswa.
   - Output: Tuple `(mahasiswa_tertinggi, mahasiswa_terendah)`.
   - Error: Jika `data` kosong, melempar `ValueError("Data kosong")`.

5. `filter_berdasarkan_grade(data: List[Mahasiswa], grade: str) -> List[Mahasiswa]`
   - Deskripsi: Mengembalikan daftar mahasiswa yang grade-nya cocok dengan parameter `grade`.
   - Input: `data`, `grade` (misal: "A").
   - Output: List mahasiswa yang memenuhi.
   - Catatan: `grade` akan diubah ke uppercase sebelum perbandingan.

6. `rata_rata_kelas(data: List[Mahasiswa]) -> float`
   - Deskripsi: Menghitung rata-rata nilai akhir seluruh mahasiswa dalam list.
   - Input: `data`.
   - Output: Rata-rata `float` dibulatkan 2 desimal. Jika `data` kosong, mengembalikan `0.0`.

7. Utilitas input
   - `_input_float(prompt: str, min_v: float = 0.0, max_v: float = 100.0) -> float`:
     - Membaca input pengguna dan memvalidasi bahwa itu angka di antara `min_v` dan `max_v`. Mengulangi prompt jika tidak valid.
   - `input_mahasiswa_baru(data: List[Mahasiswa]) -> None`:
     - Prompt interaktif untuk menambahkan satu mahasiswa baru (nama, NIM, UTS, UAS, Tugas) ke `data`.

8. `menu() -> None`
   - Deskripsi: Loop utama yang menampilkan menu interaktif dan memanggil fungsi-fungsi di atas sesuai pilihan user.
   - Opsi menu: lihat file atau lihat di awal kode.

## Kontrak singkat (inputs/outputs)

- Input utama program: interaksi via console (stdin).
- Output utama: teks tabel dan pesan ke console (stdout).
- Bentuk data mahasiswa: `dict` dengan kunci `nama`, `nim`, `nilai_uts`, `nilai_uas`, `nilai_tugas`.

## Edge cases penting

- Data kosong: `cari_tertinggi_terendah` akan melempar `ValueError`; `rata_rata_kelas` mengembalikan `0.0`.
- Input non-angka di prompt nilai: `_input_float` akan meminta ulang.
- Nilai di luar 0-100: `_input_float` menolak dan meminta ulang.
- Kunci data hilang atau format salah: fungsi penghitungan bisa melempar exception (KeyError atau ValueError). Pastikan data memiliki struktur benar.

## Dokumentasi i/o dari hasil eksekusi program
- [img/menu.png](img/menu.png) — Tampilan menu utama ketika program dijalankan.
- [img/tampilkan_semua.png](img/tampilkan_semua.png) — Tampilan output ketika memilih menu "Tampilkan semua data" (tabel lengkap semua mahasiswa).
- [img/input_mahasiswa.png](img/input_mahasiswa.png) — Tampilan proses input mahasiswa baru (prompt input dan pesan konfirmasi "Data berhasil ditambahkan!").
- [img/tertinggi_terendah.png](img/tertinggi_terendah.png) — Tampilan dua tabel: mahasiswa nilai tertinggi dan mahasiswa nilai terendah.
- [img/filter_grade_A.png](img/filter_grade_A.png) — Contoh output filter untuk grade A (tabel hasil filter untuk grade A).
- [img/rata_rata.png](img/rata_rata.png) — Tampilan output ketika menghitung rata-rata nilai kelas (baris yang mencetak "Rata-rata nilai akhir kelas: ...").
- [img/perhitungan_nilai.png](img/perhitungan_nilai.png) — (Opsional) Potongan output atau catatan debug yang menunjukkan nilai UTS/UAS/Tugas dan nilai akhir yang dihitung untuk satu mahasiswa.
- [img/keluar.png](img/keluar.png) — (Opsional) Tampilan saat memilih menu keluar yang menampilkan pesan "Terima kasih. Program selesai.".

