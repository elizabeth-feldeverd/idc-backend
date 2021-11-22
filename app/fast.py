from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tensorflow.keras.models import load_model
import numpy as np

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


@app.get("/predict")
def predict():
    model = load_model("model.h5")
    pic = np.load("raw_data/X.npy")[0:10] / 255
    prediction = [float(num) for num in model.predict(pic)[:, 0]]
    return {"prediction": prediction}


@app.get("/predict/aoi")
def areas_of_interest():
    pass


if __name__ == "__main__":
    predict()
