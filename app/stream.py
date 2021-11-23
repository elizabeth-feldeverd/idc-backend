import streamlit as st
from PIL import Image
import numpy as np
import requests
import base64
import tempfile
from tensorflow.keras.models import load_model


model = load_model("model.h5")

st.write("""bro""")


png = st.file_uploader("Upload a PNG image", type=([".png"]))


if png:

    # preprocessing

    st.image(png)
    print(type(png))
    type(png.read())
    image = Image.open(png)
    png_array = np.array(image) / 255

    pics = np.reshape(png_array, (1, 50, 50, 3))

    prediction = float(model.predict(pics)[:, 0][0])

    print(prediction)
    #     print(type(file_png_bytes))

    #     np_fullsize = np.asarray(file_png_bytes)

    # bytes_image = base64.b64encode(X[0])
    # url = "http://127.0.0.1:8000/predict"
    # response = requests.post(url, data={"file": bytes_image})
