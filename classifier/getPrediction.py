import pickle

import cv2
import numpy as np
import tensorflow as tf
# Process image and predict label
from tensorflow.python.keras.preprocessing.image import img_to_array

from static.static_var import IMG_SIZE, MODEL_PATH, CLASS_PATH


# Evaluate the model
def process_predict_image(model_path, class_path, validation_path, image_size):
    try:
        # Load the model
        model = tf.keras.models.load_model(model_path)
        # Load classes
        with open(class_path, 'rb') as file:
            loaded_class = pickle.load(file)
        # Get a list of categories

        image = cv2.imread(validation_path)
        # Get input reshaped and rescaled
        image = cv2.resize(image, (image_size, image_size))
        image_f = image.astype("float") / 255.0
        image_a = img_to_array(image_f)
        image_p = np.expand_dims(image_a, axis=0)
        # Get predictions
        predictions = model.predict(image_p).ravel()
        # Print predictions
        print(predictions)
        # Get the class with the highest probability
        prediction = np.argmax(predictions)
        # Check if the prediction is correct
        return loaded_class[prediction]
    except OSError as os:
        return os.args[0]


def processImg(img_validation_path):
    return process_predict_image(model_path=MODEL_PATH,
                                 class_path=CLASS_PATH,
                                 validation_path=img_validation_path,
                                 image_size=IMG_SIZE)
