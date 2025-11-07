from typing import List, Dict, Tuple

Mahasiswa = Dict[str, object]

# --------------------------- Data Awal ---------------------------
data_mahasiswa: List[Mahasiswa] = [
    {"nama": "Michael Mathew", "nim": "123140101", "nilai_uts": 84, "nilai_uas": 87, "nilai_tugas": 90},
    {"nama": "Mario Fransiskus Sitepu", "nim": "123140023", "nilai_uts": 72, "nilai_uas": 80, "nilai_tugas": 75},
    {"nama": "George Haansraj", "nim": "123140001", "nilai_uts": 65, "nilai_uas": 60, "nilai_tugas": 70},
    {"nama": "Faiz Akbar Al Kalabadzi", "nim": "123140091", "nilai_uts": 55, "nilai_uas": 58, "nilai_tugas": 62},
    {"nama": "Ahmad Aufamahdi Salam", "nim": "123140092", "nilai_uts": 40, "nilai_uas": 45, "nilai_tugas": 50},
]

# --------------------------- Fungsi Inti ---------------------------
def hitung_nilai_akhir(mhs: Mahasiswa) -> float:
    """Menghitung nilai akhir: 30% UTS + 40% UAS + 30% Tugas."""
    uts = float(mhs["nilai_uts"])
    uas = float(mhs["nilai_uas"])
    tugas = float(mhs["nilai_tugas"])
    return round(0.30 * uts + 0.40 * uas + 0.30 * tugas, 2)

def tentukan_grade(nilai_akhir: float) -> str:
    """Menentukan grade berdasarkan nilai akhir."""
    if nilai_akhir >= 80:
        return "A"
    elif nilai_akhir >= 70:
        return "B"
    elif nilai_akhir >= 60:
        return "C"
    elif nilai_akhir >= 50:
        return "D"
    else:
        return "E"

def _format_row(cols: List[str], widths: List[int]) -> str:
    return " | ".join(c.ljust(w) for c, w in zip(cols, widths))

def tampilkan_tabel(data: List[Mahasiswa]) -> None:
    """Menampilkan data mahasiswa dalam format tabel."""
    # Siapkan data terhitung
    rows = []
    for i, m in enumerate(data, start=1):
        na = hitung_nilai_akhir(m)
        gr = tentukan_grade(na)
        rows.append([
            str(i),
            str(m["nama"]),
            str(m["nim"]),
            f'{float(m["nilai_uts"]):.2f}',
            f'{float(m["nilai_uas"]):.2f}',
            f'{float(m["nilai_tugas"]):.2f}',
            f"{na:.2f}",
            gr,
        ])
    headers = ["No", "Nama", "NIM", "UTS", "UAS", "Tugas", "Akhir", "Grade"]
    # Hitung lebar kolom agar seragam
    widths = [max(len(h), max((len(r[i]) for r in rows), default=0)) for i, h in enumerate(headers)]
    # Cetak
    line = "-+-".join("-" * w for w in widths)
    print(_format_row(headers, widths))
    print(line)
    for r in rows:
        print(_format_row(r, widths))

def cari_tertinggi_terendah(data: List[Mahasiswa]) -> Tuple[Mahasiswa, Mahasiswa]:
    """Mengembalikan tuple (mahasiswa_tertinggi, mahasiswa_terendah) berdasarkan nilai akhir."""
    if not data:
        raise ValueError("Data kosong")
    with_scores = [(m, hitung_nilai_akhir(m)) for m in data]
    tertinggi = max(with_scores, key=lambda x: x[1])[0]
    terendah = min(with_scores, key=lambda x: x[1])[0]
    return tertinggi, terendah

def filter_berdasarkan_grade(data: List[Mahasiswa], grade: str) -> List[Mahasiswa]:
    """Mengembalikan list mahasiswa yang grade-nya sesuai."""
    grade = grade.upper()
    return [m for m in data if tentukan_grade(hitung_nilai_akhir(m)) == grade]

def rata_rata_kelas(data: List[Mahasiswa]) -> float:
    """Menghitung rata-rata nilai akhir kelas."""
    if not data:
        return 0.0
    return round(sum(hitung_nilai_akhir(m) for m in data) / len(data), 2)

# --------------------------- Utilitas Input ---------------------------
def _input_float(prompt: str, min_v: float = 0.0, max_v: float = 100.0) -> float:
    while True:
        try:
            val = float(input(prompt).replace(",", "."))
            if not (min_v <= val <= max_v):
                print(f"Nilai harus di antara {min_v} s.d. {max_v}.")
                continue
            return val
        except ValueError:
            print("Input tidak valid. Masukkan angka.")

def input_mahasiswa_baru(data: List[Mahasiswa]) -> None:
    """Meminta input user untuk menambah 1 data mahasiswa."""
    print("\n=== Input Mahasiswa Baru ===")
    nama = input("Nama        : ").strip()
    nim = input("NIM         : ").strip()
    uts = _input_float("Nilai UTS   : ")
    uas = _input_float("Nilai UAS   : ")
    tugas = _input_float("Nilai Tugas : ")
    data.append({"nama": nama, "nim": nim, "nilai_uts": uts, "nilai_uas": uas, "nilai_tugas": tugas})
    print("-> Data berhasil ditambahkan!\n")

# --------------------------- Menu Interaktif ---------------------------
def menu() -> None:
    data = data_mahasiswa  # gunakan referensi global
    while True:
        print("\n==================== MENU ====================")
        print("1. Tampilkan semua data")
        print("2. Tambah data mahasiswa baru")
        print("3. Cari mahasiswa nilai tertinggi & terendah")
        print("4. Filter mahasiswa berdasarkan grade (A/B/C/D/E)")
        print("5. Hitung rata-rata nilai kelas")
        print("6. Keluar")
        print("==============================================")
        pilih = input("Pilih menu [1-6]: ").strip()
        if pilih == "1":
            if data:
                tampilkan_tabel(data)
            else:
                print("Data kosong.")
        elif pilih == "2":
            input_mahasiswa_baru(data)
        elif pilih == "3":
            if not data:
                print("Data kosong.")
                continue
            tgh, rnd = cari_tertinggi_terendah(data)
            print("\n-- Mahasiswa Nilai Tertinggi --")
            tampilkan_tabel([tgh])
            print("\n-- Mahasiswa Nilai Terendah --")
            tampilkan_tabel([rnd])
        elif pilih == "4":
            g = input("Masukkan grade (A/B/C/D/E): ").strip().upper()
            if g not in {"A", "B", "C", "D", "E"}:
                print("Grade tidak dikenal.")
                continue
            hasil = filter_berdasarkan_grade(data, g)
            if hasil:
                print(f"\n-- Daftar Mahasiswa dengan Grade {g} --")
                tampilkan_tabel(hasil)
            else:
                print(f"Tidak ada mahasiswa dengan grade {g}.")
        elif pilih == "5":
            rata = rata_rata_kelas(data)
            print(f"Rata-rata nilai akhir kelas: {rata:.2f}")
        elif pilih == "6":
            print("Terima kasih. Program selesai.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

# --------------------------- Eksekusi ---------------------------
if __name__ == "__main__":
    menu()
