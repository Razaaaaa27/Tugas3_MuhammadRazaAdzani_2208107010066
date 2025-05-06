# 🪨📄✂️ Rock-Paper-Scissors Classification Project

**Nama:** Muhammad Raza Adzani  
**NPM:** 2208107010066

---

## 📚 Deskripsi Proyek
Proyek ini bertujuan untuk membangun sistem klasifikasi gambar sederhana menggunakan Deep Learning dengan pendekatan **Transfer Learning** menggunakan arsitektur **MobileNetV2**. Gambar yang diklasifikasikan terdiri dari tiga kategori:
- Rock
- Paper
- Scissors

Model yang dilatih akan diintegrasikan ke dalam aplikasi backend berbasis **FastAPI**, sehingga bisa menerima input gambar dan memberikan hasil prediksi secara real-time melalui REST API. Selain itu, tersedia antarmuka pengguna menggunakan **Streamlit** sebagai frontend.

---

## 🛠️ Teknologi yang Digunakan
- **TensorFlow / Keras** → Membangun dan melatih model klasifikasi
- **FastAPI** → Backend REST API
- **Uvicorn** → ASGI server untuk menjalankan FastAPI
- **Pillow (PIL)** → Pemrosesan gambar
- **NumPy** → Manipulasi data numerik
- **scikit-learn** → Evaluasi model (confusion matrix, classification report)
- **Streamlit** → Antarmuka frontend berbasis web

---

## 📂 Struktur Folder Proyek
```bash
project-root/
├── backend/
│   └── main.py              # FastAPI backend
├── frontend/
│   └── main.py              # Streamlit frontend
├── dataset/
│   ├── rock/
│   ├── paper/
│   └── scissors/
├── model/
│   └── best_transfer.keras  # Model hasil pelatihan
├── notebook.ipynb           # Notebook eksplorasi dan pelatihan
├── requirements.txt         # Daftar dependency
└── README.md                # Dokumentasi proyek
```

---

## 🚀 Langkah Penggunaan

### 1. Clone Repository
```bash
git clone https://github.com/Razaaaaa27/Tugas3_MuhammadRazaAdzani_2208107010066.git
cd Tugas3_MuhammadRazaAdzani_2208107010066
```

### 2. Setup Environment
> Rekomendasi versi Python: **3.9 – 3.11**
```bash
pip install -r requirements.txt
```

### 3. Download Dataset
Unduh dataset dari Kaggle:
📎 [https://www.kaggle.com/datasets](https://www.kaggle.com/datasets)

Ekstrak ke dalam folder `dataset/` dengan struktur berikut:
```bash
dataset/
├── rock/
├── paper/
└── scissors/
```

### 4. Jalankan Backend FastAPI
```bash
cd backend
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
> Akses API di: [http://localhost:8000/](http://localhost:8000/)

### 5. Jalankan Frontend Streamlit
```bash
cd ../frontend
streamlit run main.py
```
> Akses antarmuka pengguna di: [http://localhost:8501/](http://localhost:8501/)

---

## 🎯 Tugas Praktikum
- [x] Lengkapi bagian kode `# TODO:` pada `notebook.ipynb` dan `main.py`
- [x] Konsistenkan preprocessing antara training dan inferensi
- [x] Lakukan eksperimen kecil seperti augmentasi data dan tuning hyperparameter

---

## 📋 Catatan Penting
⚠️ Pastikan struktur folder dataset sesuai (`rock/`, `paper/`, `scissors/`)  
⚠️ Jangan lupa lengkapi semua bagian yang ditandai `# TODO`  
⚠️ Proses preprocessing saat inferensi harus identik dengan pipeline training  
