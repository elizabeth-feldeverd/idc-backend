import streamlit as st
from PIL import Image
import numpy as np
import requests
import base64
import tempfile
from idc.processing import split
import requests


st.write("""bro""")


png = st.file_uploader("Upload a PNG image", type=([".png"]))


if png:

    st.image(png)  # display image

    # preprocessing
    image = Image.open(png)
    array_of_images = split(image)

    bytes_image = base64.b64encode(array_of_images)

    url = "http://127.0.0.1:8000/predict"
    response = requests.post(url, data={"file": bytes_image})

    print(response.json())
