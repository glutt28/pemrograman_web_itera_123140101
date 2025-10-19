// ============== STATE & STORAGE ==============
let arrayTasks = [];

function loadTasks() {
  const saved = JSON.parse(localStorage.getItem('tasks'));
  arrayTasks = Array.isArray(saved) ? saved : [];
}

function saveTasks() {
  localStorage.setItem('tasks', JSON.stringify(arrayTasks));
}

// ============== DOM GETTERS ==============
const $ = (sel) => document.querySelector(sel);
const judulInput = $('#judul-tugas');
const matkulInput = $('#matkul');
const deadlineInput = $('#deadline');
const tambahBtn = $('#tambah-tugas-btn');

const cariInput = $('#cari-tugas-input');
const statusSelect = $('#cari-tugas-status');
const matkulSelect = $('#cari-tugas-matkul');
const listEl = $('#daftar-tugas-list');

// ============== HELPERS ==============
function formatDate(iso) {
  if (!iso) return '-';
  const d = new Date(iso + 'T00:00:00');
  const pad = (n) => String(n).padStart(2, '0');
  return `${pad(d.getDate())}/${pad(d.getMonth()+1)}/${d.getFullYear()}`;
}

function isValidISODate(s) {
  // Format: YYYY-MM-DD
  return /^\d{4}-\d{2}-\d{2}$/.test(s);
}

function uniqueMatkulList() {
  const set = new Set(arrayTasks.map(t => (t.matkul || '').trim()).filter(Boolean));
  return Array.from(set).sort();
}

function refreshMatkulFilterOptions() {
  const current = matkulSelect.value;
  matkulSelect.innerHTML = `<option value="semua">Semua</option>` +
    uniqueMatkulList().map(m => `<option value="${m}">${m}</option>`).join('');
  if ([...matkulSelect.options].some(o => o.value === current)) {
    matkulSelect.value = current;
  }
}

// RENDER LIST
function render() {
  const q = cariInput.value.trim().toLowerCase();
  const status = statusSelect.value;      // semua | selesai | belum-selesai
  const matkulF = matkulSelect.value;     // semua | <matkul>

  const filtered = arrayTasks.filter(t => {
    const matchText =
      t.judul.toLowerCase().includes(q) ||
      (t.matkul || '').toLowerCase().includes(q);
    const matchStatus =
      status === 'semua' ||
      (status === 'selesai' && t.selesai) ||
      (status === 'belum-selesai' && !t.selesai);
    const matchMatkul =
      matkulF === 'semua' || (t.matkul || '') === matkulF;
    return matchText && matchStatus && matchMatkul;
  });

  if (filtered.length === 0) {
    listEl.innerHTML = `<p>Tidak ada tugas.</p>`;
    return;
  }

  listEl.innerHTML = filtered.map(t => `
    <div class="tugas-item" data-id="${t.id}">
      <div class="tugas-header">
        <input type="checkbox" class="tugas-check" ${t.selesai ? 'checked' : ''} />
        <strong>${t.judul}</strong>
      </div>
      <div class="tugas-detail">
        <div><b>Mata Kuliah:</b> ${t.matkul || '-'}</div>
        <div><b>Deadline:</b> ${formatDate(t.deadline)}</div>
        <div><b>Status:</b> ${t.selesai ? 'Selesai' : 'Belum Selesai'}</div>
      </div>
      <div class="tugas-aksi">
        <button class="edit-btn">Edit</button>
        <button class="hapus-btn">Hapus</button>
      </div>
    </div>
  `).join('');

  // checkbox selesai/belum
  listEl.querySelectorAll('.tugas-check').forEach(cb => {
    cb.addEventListener('change', (e) => {
      const id = e.target.closest('.tugas-item').dataset.id;
      const idx = arrayTasks.findIndex(x => x.id === id);
      if (idx > -1) {
        arrayTasks[idx].selesai = e.target.checked;
        saveTasks();
        render();
      }
    });
  });

  // tombol hapus
  listEl.querySelectorAll('.hapus-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
      const id = e.target.closest('.tugas-item').dataset.id;
      arrayTasks = arrayTasks.filter(x => x.id !== id);
      saveTasks();
      refreshMatkulFilterOptions();
      render();
    });
  });

  // tombol edit 
  listEl.querySelectorAll('.edit-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
      const id = e.target.closest('.tugas-item').dataset.id;
      const idx = arrayTasks.findIndex(x => x.id === id);
      if (idx === -1) return;
      const cur = arrayTasks[idx];

      const newJudul = prompt('Edit Judul Tugas:', cur.judul);
      if (newJudul === null) return; // batal
      const judul = newJudul.trim();
      if (!judul) {
        alert('Judul tidak boleh kosong.');
        return;
      }

      const newMatkul = prompt('Edit Mata Kuliah (opsional):', cur.matkul || '');
      if (newMatkul === null) return; // batal
      const matkul = newMatkul.trim();

      const newDeadline = prompt('Edit Deadline (format YYYY-MM-DD):', cur.deadline || '');
      if (newDeadline === null) return; // batal
      const deadline = newDeadline.trim();
      if (!deadline || !isValidISODate(deadline)) {
        alert('Deadline harus diisi dan berformat YYYY-MM-DD.');
        return;
      }

      // update data
      arrayTasks[idx] = {
        ...cur,
        judul,
        matkul,
        deadline
      };
      saveTasks();
      refreshMatkulFilterOptions();
      render();
    });
  });
}

// ADD TASK 
function addTask() {
  const judul = (judulInput.value || '').trim();
  const matkul = (matkulInput.value || '').trim();
  const deadline = (deadlineInput.value || '').trim();

  if (!judul || !deadline) {
    alert('Judul dan Deadline wajib diisi.');
    return;
  }
  if (!isValidISODate(deadline)) {
    alert('Format deadline harus YYYY-MM-DD (contoh: 2025-10-19).');
    return;
  }

  const task = {
    id: crypto.randomUUID ? crypto.randomUUID() : String(Date.now()) + Math.random(),
    judul,
    matkul,
    deadline,
    selesai: false
  };

  arrayTasks.push(task);
  saveTasks();

  judulInput.value = '';
  matkulInput.value = '';
  deadlineInput.value = '';

  refreshMatkulFilterOptions();
  render();
}

// INIT 
document.addEventListener('DOMContentLoaded', () => {
  loadTasks();                 
  refreshMatkulFilterOptions();
  render();

  tambahBtn.addEventListener('click', addTask);
  [judulInput, matkulInput, deadlineInput].forEach(el => {
    el.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') addTask();
    });
  });

  cariInput.addEventListener('input', render);
  statusSelect.addEventListener('change', render);
  matkulSelect.addEventListener('change', render);
});
