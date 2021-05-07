import urllib
import numpy as np
import cv2
import os

def load_image(url):
    with urllib.request.urlopen(url) as response:
        image = np.asarray(bytearray(response.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    image = image[:, :, [2, 1, 0]] # BGR -> RGB
    return image

# DATA_URL_ROOT = "https://aiworkflow.s3.eu-west-3.amazonaws.com/"
# training_dataset = "sim_data"
# selected_frame = "center_2021_04_25_11_32_45_622.jpg"
# image_url = os.path.join(DATA_URL_ROOT,training_dataset+"_"+selected_frame)
# image = load_image(image_url)