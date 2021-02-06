import pickle

import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
# Process image and predict label
from tensorflow.python.keras.preprocessing.image import img_to_array

from class_names import prediction_classs

IMG_SIZE = 256
LEARNING_RATE = 0.001
COLOUR_MAP = 3
classes = prediction_classs


# Evaluate the model
def evaluate_image(model_path, class_path, valididation_path, image_size):
    # Load the model
    model = tf.keras.models.load_model(model_path)
    # Load classes
    with open(class_path, 'rb') as file:
        classes = pickle.load(file)
    # Get a list of categories

    image = cv2.imread(valididation_path)
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
    return classes[prediction]


def processImg(img_path):
    return evaluate_image(model_path=r'D:\GPUTrained\NASNetLarge\NESNetLarge_64B/NASNet_64B_331x331.h5',
                          class_path=r'D:\GPUTrained\NASNetLarge\NESNetLarge_64B/NASNet_64B_331x331.pkl',
                          valididation_path=img_path,
                          image_size=331)

# TODO Future implantation
# Create image prediction in tabular format
#     # Read image
#     model = load_model("models/resnet152_class_23_epoch_50.h5")
#     loss = tf.keras.losses.CategoricalCrossentropy()
#     optimizer = tf.keras.optimizers.Adam(learning_rate=LEARNING_RATE)
#     model.compile(optimizer=optimizer, loss=loss, metrics=['accuracy'])
#     image = cv2.imread(r"D:\test_data/" + category + '/' + name)
#     # Preprocess image
#     image = cv2.imread(IMG_PATH, 1)
#     image = cv2.resize(image, (IMG_SIZE, IMG_SIZE))
#     image = image.astype("float") / 255.0
#     image = img_to_array(image)
#     image = np.expand_dims(image, axis=0)
#     predictions = model.predict(image).ravel()
#     # Print predictions
#     print(predictions)
#     # Get the class with the highest probability
#     prediction = np.argmax(predictions)
#     # Check if the prediction is correct
#     correct = True if classes[prediction].lower() == category else False
#     # Draw the image and show the best prediction
#     image = cv2.resize(image, (256, 256))
#     cv2.putText(image, '{0}: {1} %'.format(classes[prediction], str(round(predictions[prediction] * 100, 2))),
#                 (12, 22), cv2.FONT_HERSHEY_DUPLEX, 0.7, (0, 0, 0), 2)
#     cv2.putText(image, '{0}: {1} %'.format(classes[prediction], str(round(predictions[prediction] * 100, 2))),
#                 (10, 20), cv2.FONT_HERSHEY_DUPLEX, 0.7, (65, 105, 225), 2)
#     cv2.putText(image, '{0}'.format('CORRECT!' if correct else 'WRONG!'), (12, 50), cv2.FONT_HERSHEY_DUPLEX, 0.7,
#                 (0, 0, 0), 2)
#     cv2.putText(image, '{0}'.format('CORRECT!' if correct else 'WRONG!'), (10, 48), cv2.FONT_HERSHEY_DUPLEX, 0.7,
#                 (0, 255, 0) if correct else (0, 0, 255), 2)
#
#     # Append the image
#     blocks.append(image)
#
#
# # Display images and predictions
# row1 = np.concatenate(blocks[0:3], axis=1)
# row2 = np.concatenate(blocks[3:6], axis=1)
# # cv2.imshow('Predictions', np.concatenate((row1, row2), axis=0))
# cv2.imwrite('D:/New folder/New folderpredictions_renet50.jpg', np.concatenate((row1, row2), axis=0))
# cv2.waitKey(0)
