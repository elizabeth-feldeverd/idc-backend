import numpy as np

# import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras

# from PIL import Image
# from keras.models import load_model
from keras.layers import Resizing
import matplotlib.cm as cm


def make_heatmap(img_array, model, last_conv_layer_name="conv2d_3", pred_index=None):
    # First, we create a model that maps the input image to the activations
    # of the last conv layer as well as the output predictions
    grad_model = tf.keras.models.Model(
        [model.inputs], [model.get_layer(last_conv_layer_name).output, model.output]
    )

    # Then, we compute the gradient of the top predicted class for our input image
    # with respect to the activations of the last conv layer
    with tf.GradientTape() as tape:
        last_conv_layer_output, preds = grad_model(img_array)
        if pred_index is None:
            pred_index = tf.argmax(preds[0])
        class_channel = preds[:, pred_index]

    # This is the gradient of the output neuron (top predicted or chosen)
    # with regard to the output feature map of the last conv layer
    grads = tape.gradient(class_channel, last_conv_layer_output)

    # This is a vector where each entry is the mean intensity of the gradient
    # over a specific feature map channel
    pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))

    # We multiply each channel in the feature map array
    # by "how important this channel is" with regard to the top predicted class
    # then sum all the channels to obtain the heatmap class activation

    # The line below returns only the heatmap for the first image. Keep commented.
    # last_conv_layer_output = last_conv_layer_output[0]

    heatmap = np.dot(last_conv_layer_output, pooled_grads[..., tf.newaxis])
    heatmap = tf.squeeze(heatmap)

    # Normalize the heatmap between 0 & 1
    heatmap = tf.maximum(heatmap, 0) / tf.math.reduce_max(heatmap)
    return np.uint8(heatmap.numpy() * 255)


def superimpose_heatmap(img, heatmap, alpha=1, beta=1):
    # Resize images from size of last Conv2D layer to (50, 50)
    resize = Resizing(50, 50)
    heatmap = resize(np.expand_dims(heatmap, -1))

    # Use jet colormap to colorize heatmap
    jet = cm.get_cmap("jet")

    reshaped_hm = heatmap.numpy().reshape(-1, 50, 50)

    jet_heatmap = jet(reshaped_hm/255)[:,:,:,:3]

    # create mask
    mask = heatmap > (0.44 *255)
    mask = tf.cast(mask, tf.int32).numpy()
    mask = np.repeat(mask, repeats=3 ,axis=3)

    superimposed_images = mask * jet_heatmap + (1 - mask)* img

    superimposed_images = tf.maximum(superimposed_images, 0) / tf.math.reduce_max(
            superimposed_images
        )

    # Returns an array of images with with heatmaps superimposed
    return np.uint8(255 * superimposed_images)

# if __name__ == "__main__":
#     X = np.load("raw_data/X.npy") / 255
#     # img_array = np.expand_dims(X[5], 0)
#     img_array = X[0:2]
#     model = load_model("model.h5")

#     heatmap = make_heatmap(img_array, model)
#     grad_cam = superimpose_heatmap(img_array, heatmap)

#     # print(heatmap[0])  # checking to see what the blue values look like

#     plt.subplot(2, 3, 1)
#     plt.imshow(img_array[0])
#     plt.subplot(2, 3, 2)
#     plt.imshow(heatmap[0])
#     plt.subplot(2, 3, 3)
#     plt.imshow(grad_cam[0])

#     plt.subplot(2, 3, 4)
#     plt.imshow(img_array[1])
#     plt.subplot(2, 3, 5)
#     plt.imshow(heatmap[1])
#     plt.subplot(2, 3, 6)
#     plt.imshow(grad_cam[1])

#     plt.show()
