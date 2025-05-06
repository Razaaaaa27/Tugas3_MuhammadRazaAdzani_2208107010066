import io   
import os
import uvicorn
import numpy as np
import tensorflow as tf
from PIL import Image
from pathlib import Path

from fastapi import File, UploadFile, FastAPI
from fastapi.middleware.cors import CORSMiddleware

# membuat instance FastAPI
app = FastAPI()

# izinkan request dari Streamlit
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)

# load model
BASE_DIR   = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR.parent / 'best_transfer.keras'

if os.path.exists(MODEL_PATH):
    model = tf.keras.models.load_model(str(MODEL_PATH))
else:
    raise FileNotFoundError(f"Model tidak ditemukan di {MODEL_PATH}")

# mapping indeks : label
labels = ["paper", "rock", "scissors"]
UNKNOWN_LABEL = "unknown"

# threshold confidence minimum
THRESHOLD = 0.6

def preprocess_pipeline(image: Image.Image, IMG_SIZE = (224, 224)) -> np.ndarray:
    """
    Fungsi untuk melakukan preprocessing pada gambar input.
    Praktikan diminta untuk:
    - Melakukan resize gambar ke IMG_SIZE.
    - Mengubah gambar menjadi array bertipe float32.
    - Melakukan rescaling pixel dari [0,255] ke [0,1].
    """
    
    # Resize gambar ke ukuran yang sesuai
    image = image.resize(IMG_SIZE)
    
    # Konversi ke array numpy
    arr = np.array(image, dtype=np.float32)
    
    # Normalisasi pixel dari [0,255] ke [0,1]
    arr = arr / 255.0
    
    return arr  # mengembalikan array hasil preprocessing

# endpoint untuk menerima input dan menghasilkan prediksi
@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()

    image = Image.open(io.BytesIO(contents)).convert("RGB")
    x = preprocess_pipeline(image)
    x = np.expand_dims(x, axis=0)

    predictions = model.predict(x)
    best_index = int(np.argmax(predictions[0]))
    confidence = float(predictions[0][best_index])

    if confidence < THRESHOLD:
        label = UNKNOWN_LABEL
    else:
        label = labels[best_index]

    return {"label": label, "confidence": confidence}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)