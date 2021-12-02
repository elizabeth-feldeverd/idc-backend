from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
from idc.processing import split, stitch
from idc.gradcam import make_heatmap, superimpose_heatmap
from idc.report import model_report, recommend
from google.cloud import storage
import uuid


app = FastAPI()
model = load_model("model.h5")
IDC_BUCKET = "idc_bucket"


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


@app.post("/annotate")
def annotate(file: UploadFile = File(...)):

    image = Image.open(file.file)
    height, width, _ = np.asarray(image).shape

    round_height = int(np.ceil(height / 50))
    round_width = int(np.ceil(width / 50))

    pics = split(image) / 255
    heatmap = make_heatmap(pics, model)
    grad_cam = superimpose_heatmap(pics, heatmap)

    # stitch image together
    high_image = stitch(grad_cam, round_height * 50, round_width * 50)[
        :height,
        :width,
    ]

    # save the image as a png
    myuuid = uuid.uuid4()
    path = f"{myuuid}.png"
    im = Image.fromarray(high_image)  # this hsould be high_image
    im.save(path)

    # upload png to google cloud storage
    gcs = storage.Client()
    bucket = gcs.get_bucket(IDC_BUCKET)
    blob = bucket.blob(path)
    blob.upload_from_filename(path)

    # produce report
    prediction = model.predict(pics)
    report = model_report(prediction)

    # produce recommendation
    recommendation = recommend(report)

    return {"url": blob.public_url, "report": report, "recommendation": recommendation}
