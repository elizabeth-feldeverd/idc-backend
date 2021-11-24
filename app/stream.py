import streamlit as st
from PIL import Image
import numpy as np
import requests
import base64
import tempfile
from tensorflow.keras.models import load_model
from idc.processing import split


model = load_model("model.h5")

st.write("""bro""")


png = st.file_uploader("Upload a PNG image", type=([".png"]))


if png:

    # preprocessing

    st.image(png)
    print(type(png))
    type(png.read())
    image = Image.open(png)

    array_of_images = split(image)

    scaled_images = array_of_images / 255

    prediction = model.predict(scaled_images)[:, 0]

    r = prediction.tolist()

    print(r)
