# Rock-Paper-Scissors Classification Project 🪨📄✂️

📚 Deskripsi Proyek
────────────────────
Proyek ini bertujuan untuk membangun sistem klasifikasi gambar sederhana
menggunakan Deep Learning dengan arsitektur Transfer Learning (MobileNetV2).
Gambar yang diklasifikasikan terdiri dari tiga kategori:
  - Rock
  - Paper
  - Scissors

Model yang dilatih kemudian akan diintegrasikan ke dalam aplikasi backend
berbasis FastAPI agar bisa menerima gambar dan memberikan hasil prediksi
secara real-time.

🛠️ Teknologi yang Digunakan
────────────────────────────
• TensorFlow / Keras       → Membangun dan melatih model klasifikasi
• FastAPI                  → Backend REST API
• Uvicorn                  → ASGI server untuk menjalankan FastAPI
• PIL (Pillow)             → Memproses gambar input
• NumPy                    → Manipulasi array numerik
• scikit-learn             → Evaluasi model (confusion matrix, report)
• Streamlit                → Frontend antarmuka pengguna

📂 Struktur Folder Proyek
──────────────────────────
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
├── requirements.txt         # Dependency
└── README.md                # Dokumentasi proyek

🚀 Langkah Penggunaan
──────────────────────
1. Clone repository
$ git clone https://github.com/Razaaaaa27/Tugas3_MuhammadRazaAdzani_2208107010066.git
$ cd Tugas3_MuhammadRazaAdzani_2208107010066

2. Setup environment
(rekomendasi Python 3.9 – 3.11)
$ pip install -r requirements.txt

3. Download Dataset dari Kaggle
📎 https://www.kaggle.com/datasets

Struktur setelah ekstrak:
dataset/
├── rock/
├── paper/
└── scissors/

4. Jalankan backend FastAPI
$ cd backend
$ uvicorn main:app --host 0.0.0.0 --port 8000 --reload

→ Akses API di: http://localhost:8000/

5. Jalankan frontend Streamlit
$ cd ../frontend
$ streamlit run main.py

→ Akses antarmuka di: http://localhost:8501/

🎯 Tugas Praktikum
──────────────────
✓ Lengkapi bagian kode `# TODO:` pada `notebook.ipynb` dan `main.py`
✓ Konsistenkan preprocessing antara training dan inferensi
✓ Lakukan eksperimen kecil (augmentasi, tuning hyperparameter)

📋 Catatan Penting
──────────────────
⚠️ Pastikan struktur folder dataset benar (rock/, paper/, scissors/)
⚠️ Jangan lupa isi semua bagian TODO
⚠️ Preprocessing saat inferensi harus sama dengan training pipeline
