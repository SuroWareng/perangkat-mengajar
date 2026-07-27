// Counter untuk ID unik
let protaMaterialCount = 0;
let promesKDCount = 0;
let promesDistribusiCount = 0;

// ==================== PROTA FUNCTIONS ====================

function addProtaMaterial() {
    protaMaterialCount++;
    const html = `
        <div class="card mt-2" id="material-${protaMaterialCount}">
            <div class="card-body">
                <button type="button" class="btn btn-danger btn-sm float-end" onclick="removeProtaMaterial(${protaMaterialCount})">
                    <i class="fas fa-trash"></i> Hapus
                </button>
                <div class="row">
                    <div class="col-md-3">
                        <label class="form-label">Semester</label>
                        <select class="form-control" name="materis[${protaMaterialCount}][semester]" required>
                            <option value="">Pilih</option>
                            <option value="1">Semester 1</option>
                            <option value="2">Semester 2</option>
                        </select>
                    </div>
                    <div class="col-md-3">
                        <label class="form-label">Kompetensi Dasar</label>
                        <input type="text" class="form-control" name="materis[${protaMaterialCount}][kd]" placeholder="3.1" required>
                    </div>
                    <div class="col-md-4">
                        <label class="form-label">Materi Pokok</label>
                        <input type="text" class="form-control" name="materis[${protaMaterialCount}][materi]" placeholder="Nama Materi" required>
                    </div>
                    <div class="col-md-2">
                        <label class="form-label">Jam (JP)</label>
                        <input type="number" class="form-control" name="materis[${protaMaterialCount}][jam]" min="1" value="2" required>
                    </div>
                </div>
            </div>
        </div>
    `;
    document.getElementById('protaMaterialList').insertAdjacentHTML('beforeend', html);
}

function removeProtaMaterial(id) {
    document.getElementById(`material-${id}`).remove();
}

function getFormData(formId) {
    const form = document.getElementById(formId);
    const formData = new FormData(form);
    const data = {};
    
    formData.forEach((value, key) => {
        if (key.includes('[')) {
            // Handle array data
            const arrayMatch = key.match(/^(.+?)\[(\d+)\]\[(.+)\]$/);
            if (arrayMatch) {
                const arrayName = arrayMatch[1];
                const index = parseInt(arrayMatch[2]);
                const fieldName = arrayMatch[3];
                
                if (!data[arrayName]) data[arrayName] = {};
                if (!data[arrayName][index]) data[arrayName][index] = {};
                data[arrayName][index][fieldName] = value;
            }
        } else {
            data[key] = value;
        }
    });
    
    // Convert object to array
    if (data.materis) {
        data.materis = Object.values(data.materis);
    }
    if (data.kds) {
        data.kds = Object.values(data.kds);
    }
    if (data.distribusi) {
        data.distribusi = Object.values(data.distribusi);
    }
    
    return data;
}

function saveProtaData() {
    const data = getFormData('protaForm');
    fetch('/api/prota', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        showNotification('Data Prota berhasil disimpan!');
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error: ' + error);
    });
}

function exportProtaWord() {
    const data = getFormData('protaForm');
    fetch('/api/export/prota-word', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.blob())
    .then(blob => {
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `Prota_${data.mata_pelajaran}_${new Date().toISOString().slice(0,10)}.docx`;
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
        showNotification('File Prota Word berhasil diunduh!');
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error: ' + error);
    });
}

function exportProtaExcel() {
    const data = getFormData('protaForm');
    fetch('/api/export/prota-excel', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.blob())
    .then(blob => {
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `Prota_${data.mata_pelajaran}_${new Date().toISOString().slice(0,10)}.xlsx`;
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
        showNotification('File Prota Excel berhasil diunduh!');
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error: ' + error);
    });
}

// ==================== PROMES FUNCTIONS ====================

function addPromesKD() {
    promesKDCount++;
    const html = `
        <div class="card mt-2" id="kd-${promesKDCount}">
            <div class="card-body">
                <button type="button" class="btn btn-danger btn-sm float-end" onclick="removePromesKD(${promesKDCount})">
                    <i class="fas fa-trash"></i> Hapus
                </button>
                <div class="row">
                    <div class="col-md-4">
                        <label class="form-label">Kompetensi Dasar</label>
                        <input type="text" class="form-control" name="kds[${promesKDCount}][kd]" placeholder="3.1" required>
                    </div>
                    <div class="col-md-8">
                        <label class="form-label">Materi Pokok</label>
                        <input type="text" class="form-control" name="kds[${promesKDCount}][materi]" placeholder="Nama Materi" required>
                    </div>
                </div>
            </div>
        </div>
    `;
    document.getElementById('promesKDList').insertAdjacentHTML('beforeend', html);
}

function removePromesKD(id) {
    document.getElementById(`kd-${id}`).remove();
}

function addPromesDistribusi() {
    promesDistribusiCount++;
    const bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember'];
    
    const html = `
        <div class="card mt-2" id="dist-${promesDistribusiCount}">
            <div class="card-body">
                <button type="button" class="btn btn-danger btn-sm float-end" onclick="removePromesDistribusi(${promesDistribusiCount})">
                    <i class="fas fa-trash"></i> Hapus
                </button>
                <div class="row">
                    <div class="col-md-3">
                        <label class="form-label">Bulan</label>
                        <select class="form-control" name="distribusi[${promesDistribusiCount}][bulan]" required>
                            <option value="">Pilih Bulan</option>
                            ${bulan.map((b, i) => `<option value="${b}">${b}</option>`).join('')}
                        </select>
                    </div>
                    <div class="col-md-2">
                        <label class="form-label">Minggu</label>
                        <input type="number" class="form-control" name="distribusi[${promesDistribusiCount}][minggu]" min="1" max="5" required>
                    </div>
                    <div class="col-md-3">
                        <label class="form-label">KD</label>
                        <input type="text" class="form-control" name="distribusi[${promesDistribusiCount}][kd]" placeholder="3.1" required>
                    </div>
                    <div class="col-md-2">
                        <label class="form-label">JP</label>
                        <input type="number" class="form-control" name="distribusi[${promesDistribusiCount}][jam]" min="1" value="2" required>
                    </div>
                    <div class="col-md-2">
                        <label class="form-label">Ket</label>
                        <input type="text" class="form-control" name="distribusi[${promesDistribusiCount}][keterangan]" placeholder="Libur/Cadangan">
                    </div>
                </div>
            </div>
        </div>
    `;
    document.getElementById('promesDistribusiList').insertAdjacentHTML('beforeend', html);
}

function removePromesDistribusi(id) {
    document.getElementById(`dist-${id}`).remove();
}

function savePromesData() {
    const data = getFormData('promesForm');
    fetch('/api/promes', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        showNotification('Data Promes berhasil disimpan!');
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error: ' + error);
    });
}

// ==================== MODUL FUNCTIONS ====================

function saveModulData() {
    const data = getFormData('modulForm');
    fetch('/api/modul', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        showNotification('Data Modul berhasil disimpan!');
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error: ' + error);
    });
}

function exportModulWord() {
    const data = getFormData('modulForm');
    fetch('/api/export/modul-word', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.blob())
    .then(blob => {
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `Modul_${data.judul_modul}_${new Date().toISOString().slice(0,10)}.docx`;
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
        showNotification('File Modul Word berhasil diunduh!');
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error: ' + error);
    });
}

// ==================== UTILITY FUNCTIONS ====================

function showNotification(message) {
    const notification = document.createElement('div');
    notification.className = 'success-message';
    notification.textContent = message;
    document.body.appendChild(notification);
    notification.style.display = 'block';
    
    setTimeout(() => {
        notification.style.display = 'none';
        notification.remove();
    }, 3000);
}

// Initialize pada saat page load
document.addEventListener('DOMContentLoaded', function() {
    // Add minimal 1 material row for Prota
    addProtaMaterial();
    addPromesKD();
    addPromesDistribusi();
});
