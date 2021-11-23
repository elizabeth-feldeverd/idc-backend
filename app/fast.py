from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from tensorflow.keras.models import load_model
import numpy as np
from pydantic import BaseModel
from PIL import Image  # encode into a bytesIO and #decode
from io import BytesIO
from typing import Optional
import base64


# class Item(BaseModel):
#     picbytes: bytes


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.post("/items/")
async def create_item(file: bytes = File(...)):
    # decoding
    return file


@app.get("/")
def index():
    return {"greeting": "Hello nadia"}


@app.post("/predict")
def predict(file: bytes = File(...)):

    file_decode = base64.b64decode(file)
    long_array = np.frombuffer(file_decode, dtype=np.uint8)

    pic = np.reshape(long_array, (50, 50, 3)) / 255

    pics = np.reshape(pic, (1, 50, 50, 3))

    model = load_model("model.h5")

    prediction = float(model.predict(pics)[:, 0][0])

    # prediction = [float(num) for num in model.predict(pic)[:, 0]]
    return {"prediction": prediction}


# @app.get("/predict/aoi")
# def areas_of_interest():
#     pass


if __name__ == "__main__":
    predict()
