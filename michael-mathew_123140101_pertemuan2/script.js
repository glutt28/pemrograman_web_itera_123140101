// -------------------------
// 1. Class untuk data jadwal
// -------------------------
class JadwalItem {
  constructor(matkul, hari, jam) {
    this.matkul = matkul;
    this.hari = hari;
    this.jam = jam;
  }
}

// -------------------------
// 2. State aplikasi
// -------------------------
let daftarJadwal = []; // array of JadwalItem

// Elemen DOM
const form = document.getElementById("jadwal-form");
const inputMatkul = document.getElementById("matkul");
const inputHari = document.getElementById("hari");
const inputJam = document.getElementById("jam");
const inputEditIndex = document.getElementById("edit-index");
const tombolSubmit = document.getElementById("submit-btn");
const wadahList = document.getElementById("jadwal-list");
const waktuSekarangEl = document.getElementById("waktu-sekarang");

// -------------------------
// 3. Utilitas Local Storage
// -------------------------
const SIMPAN_KEY = "jadwal_kuliah_mathew";

// simpan data ke localStorage
const simpanKeStorage = () => {
  localStorage.setItem(SIMPAN_KEY, JSON.stringify(daftarJadwal));
};

// ambil data dari localStorage
const muatDariStorage = () => {
  const dataString = localStorage.getItem(SIMPAN_KEY);
  if (dataString) {
    // parse lalu mapping lagi jadi instance JadwalItem
    const arr = JSON.parse(dataString);
    daftarJadwal = arr.map(item => new JadwalItem(item.matkul, item.hari, item.jam));
  } else {
    daftarJadwal = [];
  }
};

// -------------------------
// 4. Render daftar jadwal ke halaman
// -------------------------
const renderJadwal = () => {
  if (daftarJadwal.length === 0) {
    wadahList.innerHTML = `<p style="color:#94a3b8;font-size:0.85rem;">Belum ada jadwal. Tambahkan di form di atas.</p>`;
    return;
  }

  // build HTML list pakai template literals
  let htmlGabungan = "";
  daftarJadwal.forEach((item, index) => {
    htmlGabungan += `
      <div class="jadwal-item">
        <div class="jadwal-info">
          <div class="matkul">${item.matkul}</div>
          <div class="detail">${item.hari} • ${item.jam}</div>
        </div>
        <div class="actions">
          <button class="btn-kecil btn-edit" onclick="editJadwal(${index})">Edit</button>
          <button class="btn-kecil btn-hapus" onclick="hapusJadwal(${index})">Hapus</button>
        </div>
      </div>
    `;
  });

  wadahList.innerHTML = htmlGabungan;
};

// -------------------------
// 5. Tambah / Update data
// -------------------------
const resetForm = () => {
  inputMatkul.value = "";
  inputHari.value = "";
  inputJam.value = "";
  inputEditIndex.value = "";
  tombolSubmit.textContent = "Simpan Jadwal";
};

// ketika submit form
form.addEventListener("submit", (event) => {
  event.preventDefault();

  const matkulBaru = inputMatkul.value.trim();
  const hariBaru = inputHari.value;
  const jamBaru = inputJam.value;
  const editIndex = inputEditIndex.value;

  if (!matkulBaru || !hariBaru || !jamBaru) {
    alert("Isi semua field dulu ya 🙏");
    return;
  }

  if (editIndex === "") {
    // mode tambah
    const itemBaru = new JadwalItem(matkulBaru, hariBaru, jamBaru);
    daftarJadwal.push(itemBaru);
  } else {
    // mode edit
    const idx = Number(editIndex);
    daftarJadwal[idx].matkul = matkulBaru;
    daftarJadwal[idx].hari = hariBaru;
    daftarJadwal[idx].jam = jamBaru;
  }

  simpanKeStorage();
  renderJadwal();
  resetForm();
});

// fungsi dipanggil tombol Edit
const editJadwal = (index) => {
  const item = daftarJadwal[index];
  inputMatkul.value = item.matkul;
  inputHari.value = item.hari;
  inputJam.value = item.jam;
  inputEditIndex.value = index;
  tombolSubmit.textContent = "Update Jadwal";
};

// fungsi dipanggil tombol Hapus
const hapusJadwal = (index) => {
  const yakin = confirm(`Hapus jadwal "${daftarJadwal[index].matkul}"?`);
  if (!yakin) return;

  daftarJadwal.splice(index, 1);
  simpanKeStorage();
  renderJadwal();
};

// Penting: supaya editJadwal & hapusJadwal bisa di-akses dari HTML onclick,
// kita simpan ke window (cara simpel tanpa module bundler)
window.editJadwal = editJadwal;
window.hapusJadwal = hapusJadwal;

// -------------------------
// 6. Fitur Asinkron (async/await)
// -------------------------
// Kita bikin fungsi async yang "mengambil waktu sekarang" dengan delay pura-pura,
// seolah-olah fetch dari API jam dunia.
const delay = (ms) =>
  new Promise((resolve) => {
    setTimeout(() => resolve(), ms);
  });

// arrow function async
const updateWaktuSekarang = async () => {
  // tunggu 500ms biar keliatan asinkron
  await delay(500);

  const sekarang = new Date();
  // contoh template literal
  const jam = String(sekarang.getHours()).padStart(2, "0");
  const menit = String(sekarang.getMinutes()).padStart(2, "0");
  const detik = String(sekarang.getSeconds()).padStart(2, "0");

  waktuSekarangEl.textContent = `Waktu sekarang: ${jam}:${menit}:${detik} WIB`;
};

// jalanin update jam tiap 1 detik
setInterval(updateWaktuSekarang, 1000);

// -------------------------
// 7. Inisialisasi saat halaman dibuka
// -------------------------
const init = () => {
  muatDariStorage();
  renderJadwal();
  updateWaktuSekarang();
};

init();
