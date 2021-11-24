import numpy as np
import pandas as pd
from sklearn.feature_extraction import image
import matplotlib.pyplot as plt
from PIL import Image
from numpy import asarray


def split(image):
    # Convert image to nparray
    X = asarray(image)
    # Get image dimensions
    height = X.shape[0]
    width = X.shape[1]
    # Pad image with white so its dimensions are multiples of 50. Assumes an RGB image
    pad_height = int(np.ceil(height / 50)) * 50
    pad_width = int(np.ceil(width / 50)) * 50
    pad = np.ones((pad_height, pad_width, 3), dtype=np.uint8) * 255
    pad[:height, :width, :] = X
    # Create an array of 50 x 50 images
    img_array = np.zeros(
        (int(pad_height / 50) * int(pad_width / 50), 50, 50, 3), dtype=np.uint8
    )
    for h in range(int(pad_height / 50)):
        for w in range(int(pad_width / 50)):
            img_array[h * int(pad_width / 50) + w, :, :, :] = pad[
                h * 50 : (h + 1) * 50, w * 50 : (w + 1) * 50, :
            ]
    return img_array


def stitch(array, pad_height, pad_width):
    # Create an array of 255 that is the same size as the padded image
    new_img_array = np.ones((pad_height, pad_width, 3), dtype=np.uint8) * 255
    width_div_50 = int(pad_width / 50)
    for h in range(int(pad_height / 50)):
        for w in range(int(pad_width / 50)):
            new_img_array[h * 50 : (h + 1) * 50, w * 50 : (w + 1) * 50, :] = array[
                h * width_div_50 + w
            ]
    return new_img_array


# if __name__ == "__main__":
#     image = Image.open('../idc/data/10253_idx5.png') # Change for actual images
#     data = create_img_array(image)
#     print(data.shape)
#     new_img_array = create_img_from_array(data, 2250, 2750)
#     print(new_img_array.shape)
