from flask import Flask, render_template, request, jsonify, send_file
from flask_cors import CORS
import json
import os
from datetime import datetime
from io import BytesIO
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

app = Flask(__name__)
CORS(app)

# Folder untuk menyimpan data
DATA_FOLDER = 'data'
if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)

# ==================== ROUTES ====================

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/prota', methods=['GET', 'POST'])
def prota():
    if request.method == 'POST':
        data = request.json
        # Simpan data
        filename = f"{DATA_FOLDER}/prota_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return jsonify({"status": "success", "message": "Data Prota disimpan", "file": filename})
    
    return jsonify({"status": "error"})

@app.route('/api/promes', methods=['GET', 'POST'])
def promes():
    if request.method == 'POST':
        data = request.json
        filename = f"{DATA_FOLDER}/promes_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return jsonify({"status": "success", "message": "Data Promes disimpan", "file": filename})
    
    return jsonify({"status": "error"})

@app.route('/api/modul', methods=['GET', 'POST'])
def modul():
    if request.method == 'POST':
        data = request.json
        filename = f"{DATA_FOLDER}/modul_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return jsonify({"status": "success", "message": "Data Modul disimpan", "file": filename})
    
    return jsonify({"status": "error"})

# ==================== EXPORT FUNCTIONS ====================

@app.route('/api/export/prota-word', methods=['POST'])
def export_prota_word():
    """Export Prota ke format Word"""
    data = request.json
    
    doc = Document()
    
    # Header
    title = doc.add_paragraph()
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = title.add_run('PROGRAM TAHUNAN (PROTA)')
    run.font.size = Pt(14)
    run.font.bold = True
    
    # Identitas Sekolah
    doc.add_heading('I. IDENTITAS SEKOLAH', level=2)
    table = doc.add_table(rows=9, cols=2)
    table.style = 'Light Grid Accent 1'
    
    identitas = [
        ('Nama Sekolah', data.get('nama_sekolah', '')),
        ('Alamat', data.get('alamat', '')),
        ('Kota', data.get('kota', '')),
        ('Provinsi', data.get('provinsi', '')),
        ('Mata Pelajaran', data.get('mata_pelajaran', '')),
        ('Kelas/Semester', data.get('kelas', '')),
        ('Tahun Ajaran', data.get('tahun_ajaran', '')),
        ('Nama Guru', data.get('nama_guru', '')),
        ('NIP', data.get('nip', ''))
    ]
    
    for i, (label, value) in enumerate(identitas):
        table.rows[i].cells[0].text = label
        table.rows[i].cells[1].text = value
    
    # Kompetensi Inti
    doc.add_heading('II. KOMPETENSI INTI', level=2)
    doc.add_paragraph(f"KI-1: {data.get('ki1', '')}", style='List Bullet')
    doc.add_paragraph(f"KI-2: {data.get('ki2', '')}", style='List Bullet')
    doc.add_paragraph(f"KI-3: {data.get('ki3', '')}", style='List Bullet')
    doc.add_paragraph(f"KI-4: {data.get('ki4', '')}", style='List Bullet')
    
    # Materi Pokok
    doc.add_heading('III. KOMPETENSI DASAR DAN MATERI POKOK', level=2)
    table = doc.add_table(rows=1, cols=5)
    table.style = 'Light Grid Accent 1'
    
    # Header
    header_cells = table.rows[0].cells
    headers = ['No', 'Semester', 'Kompetensi Dasar', 'Materi Pokok', 'Alokasi Waktu (JP)']
    for i, header in enumerate(headers):
        header_cells[i].text = header
        for paragraph in header_cells[i].paragraphs:
            for run in paragraph.runs:
                run.font.bold = True
    
    # Data materi
    materis = data.get('materis', [])
    for i, materi in enumerate(materis, 1):
        row_cells = table.add_row().cells
        row_cells[0].text = str(i)
        row_cells[1].text = materi.get('semester', '')
        row_cells[2].text = materi.get('kd', '')
        row_cells[3].text = materi.get('materi', '')
        row_cells[4].text = str(materi.get('jam', ''))
    
    # Total alokasi waktu
    doc.add_heading('IV. TOTAL ALOKASI WAKTU', level=2)
    total_s1 = sum([int(m.get('jam', 0)) for m in materis if m.get('semester') == '1'])
    total_s2 = sum([int(m.get('jam', 0)) for m in materis if m.get('semester') == '2'])
    doc.add_paragraph(f"Semester 1: {total_s1} Jam Pelajaran")
    doc.add_paragraph(f"Semester 2: {total_s2} Jam Pelajaran")
    doc.add_paragraph(f"Total: {total_s1 + total_s2} Jam Pelajaran")
    doc.add_paragraph(f"\nKeterangan: {data.get('keterangan', '')}")
    
    # Tanda tangan
    doc.add_page_break()
    table = doc.add_table(rows=4, cols=2)
    table.rows[0].cells[0].text = 'Mengetahui,'
    table.rows[0].cells[0].text = 'Mengetahui,'
    table.rows[1].cells[0].text = 'Kepala Sekolah'
    table.rows[1].cells[1].text = 'Guru Mata Pelajaran'
    table.rows[3].cells[0].text = f"NIP. {data.get('nip_kepsek', '')}"
    table.rows[3].cells[1].text = f"NIP. {data.get('nip', '')}"
    
    # Save to BytesIO
    output = BytesIO()
    doc.save(output)
    output.seek(0)
    
    return send_file(
        output,
        mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        as_attachment=True,
        download_name=f"Prota_{data.get('mata_pelajaran', 'Pelajaran')}_{datetime.now().strftime('%Y%m%d')}.docx"
    )

@app.route('/api/export/prota-excel', methods=['POST'])
def export_prota_excel():
    """Export Prota ke format Excel"""
    data = request.json
    
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = 'Prota'
    
    # Style
    header_fill = PatternFill(start_color='4472C4', end_color='4472C4', fill_type='solid')
    header_font = Font(bold=True, color='FFFFFF')
    border = Border(
        left=Side(style='thin'),
        right=Side(style='thin'),
        top=Side(style='thin'),
        bottom=Side(style='thin')
    )
    
    # Title
    ws['A1'] = 'PROGRAM TAHUNAN (PROTA)'
    ws['A1'].font = Font(bold=True, size=14)
    
    # Identitas
    row = 3
    ws[f'A{row}'] = 'IDENTITAS SEKOLAH'
    ws[f'A{row}'].font = Font(bold=True)
    
    row += 1
    identitas_data = [
        ('Nama Sekolah', data.get('nama_sekolah', '')),
        ('Mata Pelajaran', data.get('mata_pelajaran', '')),
        ('Kelas', data.get('kelas', '')),
        ('Tahun Ajaran', data.get('tahun_ajaran', '')),
        ('Guru', data.get('nama_guru', '')),
    ]
    
    for label, value in identitas_data:
        ws[f'A{row}'] = label
        ws[f'B{row}'] = value
        ws[f'A{row}'].font = Font(bold=True)
        row += 1
    
    # Tabel Materi
    row += 1
    ws[f'A{row}'] = 'KOMPETENSI DASAR DAN MATERI POKOK'
    ws[f'A{row}'].font = Font(bold=True)
    
    row += 1
    headers = ['No', 'Semester', 'Kompetensi Dasar', 'Materi Pokok', 'Alokasi Waktu (JP)']
    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=row, column=col)
        cell.value = header
        cell.fill = header_fill
        cell.font = header_font
        cell.border = border
        cell.alignment = Alignment(horizontal='center', vertical='center')
    
    row += 1
    materis = data.get('materis', [])
    for i, materi in enumerate(materis, 1):
        ws.cell(row=row, column=1).value = i
        ws.cell(row=row, column=2).value = materi.get('semester', '')
        ws.cell(row=row, column=3).value = materi.get('kd', '')
        ws.cell(row=row, column=4).value = materi.get('materi', '')
        ws.cell(row=row, column=5).value = int(materi.get('jam', 0))
        
        for col in range(1, 6):
            ws.cell(row=row, column=col).border = border
        
        row += 1
    
    # Adjust column widths
    ws.column_dimensions['A'].width = 5
    ws.column_dimensions['B'].width = 12
    ws.column_dimensions['C'].width = 25
    ws.column_dimensions['D'].width = 30
    ws.column_dimensions['E'].width = 15
    
    # Save
    output = BytesIO()
    wb.save(output)
    output.seek(0)
    
    return send_file(
        output,
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        as_attachment=True,
        download_name=f"Prota_{data.get('mata_pelajaran', 'Pelajaran')}_{datetime.now().strftime('%Y%m%d')}.xlsx"
    )

@app.route('/api/export/modul-word', methods=['POST'])
def export_modul_word():
    """Export Modul Ajar ke format Word"""
    data = request.json
    
    doc = Document()
    
    # Title
    title = doc.add_paragraph()
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = title.add_run('MODUL AJAR')
    run.font.size = Pt(14)
    run.font.bold = True
    
    subtitle = doc.add_paragraph()
    subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = subtitle.add_run(data.get('judul_modul', ''))
    run.font.size = Pt(12)
    run.font.bold = True
    
    # A. INFORMASI UMUM
    doc.add_heading('A. INFORMASI UMUM', level=2)
    table = doc.add_table(rows=1, cols=2)
    table.style = 'Light Grid Accent 1'
    
    informasi = [
        ('Nama Penyusun', data.get('nama_penyusun', '')),
        ('Sekolah', data.get('sekolah', '')),
        ('Kelas', data.get('kelas', '')),
        ('Alokasi Waktu', f"{data.get('alokasi_waktu', '')} Jam Pelajaran"),
        ('Mata Pelajaran', data.get('mata_pelajaran', '')),
        ('Kompetensi Dasar', data.get('kd', '')),
    ]
    
    for label, value in informasi:
        row = table.add_row()
        row.cells[0].text = label
        row.cells[1].text = value
    
    # B. KOMPONEN INTI
    doc.add_heading('B. KOMPONEN INTI', level=2)
    
    doc.add_heading('1. Tujuan Pembelajaran', level=3)
    doc.add_paragraph(data.get('tujuan_pembelajaran', ''), style='List Bullet')
    
    doc.add_heading('2. Pemahaman Bermakna', level=3)
    doc.add_paragraph(f"Konsep Utama: {data.get('pemahaman_konsep', '')}")
    doc.add_paragraph(f"Relevansi: {data.get('pemahaman_relevansi', '')}")
    
    doc.add_heading('3. Pertanyaan Pemantik', level=3)
    pertanyaan_list = data.get('pertanyaan_pemantik', '').split('\n')
    for q in pertanyaan_list:
        if q.strip():
            doc.add_paragraph(q.strip(), style='List Bullet')
    
    doc.add_heading('4. Kegiatan Pembelajaran', level=3)
    doc.add_paragraph(data.get('kegiatan_pembelajaran', ''))
    
    doc.add_heading('5. Asesmen/Penilaian', level=3)
    doc.add_paragraph(f"Formatif: {data.get('penilaian_formatif', '')}")
    doc.add_paragraph(f"Sumatif: {data.get('penilaian_sumatif', '')}")
    
    doc.add_heading('6. Refleksi Peserta Didik', level=3)
    doc.add_paragraph(data.get('refleksi', ''))
    
    # C. LAMPIRAN
    doc.add_heading('C. LAMPIRAN', level=2)
    doc.add_heading('1. Lembar Kerja Peserta Didik (LKPD)', level=3)
    doc.add_paragraph(data.get('lkpd', ''))
    
    doc.add_heading('2. Sumber Belajar', level=3)
    sumber_list = data.get('sumber_belajar', '').split('\n')
    for s in sumber_list:
        if s.strip():
            doc.add_paragraph(s.strip(), style='List Bullet')
    
    # Save
    output = BytesIO()
    doc.save(output)
    output.seek(0)
    
    return send_file(
        output,
        mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        as_attachment=True,
        download_name=f"Modul_{data.get('judul_modul', 'Ajar')}_{datetime.now().strftime('%Y%m%d')}.docx"
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
