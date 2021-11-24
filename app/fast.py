from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from tensorflow.keras.models import load_model
import numpy as np
from pydantic import BaseModel
from PIL import Image  # encode into a bytesIO and #decode
from io import BytesIO
from typing import Optional
import base64
from idc.processing import split
from idc.gradcam import make_gradcam_heatmap, save_and_display_gradcam


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.get("/")
def index():
    return {"greeting": "Hello nadia"}


@app.post("/predict")
def predict(file: bytes = File(...)):

    file_decode = base64.b64decode(file)
    long_array = np.frombuffer(file_decode, dtype=np.uint8)

    count = long_array.shape[0] // 7500
    pics = np.reshape(long_array, (count, 50, 50, 3)) / 255

    model = load_model("model.h5")

    prediction = float(model.predict(pics)[:, 0][0])

    prediction = [float(num) for num in model.predict(pics)[:, 0]]
    return {"prediction": prediction}


@app.post("/annotate")
def annotate(file: bytes = File(...)):

    file_decode = base64.b64decode(file)
    long_array = np.frombuffer(file_decode, dtype=np.uint8)

    count = long_array.shape[0] // 7500
    pics = np.reshape(long_array, (count, 50, 50, 3)) / 255

    model = load_model("model.h5")

    prediction = float(model.predict(pics)[:, 0][0])

    prediction = [float(num) for num in model.predict(pics)[:, 0]]
    return {"prediction": prediction}


if __name__ == "__main__":
    annotate()
