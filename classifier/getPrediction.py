import pickle
import numpy as np
import tensorflow as tf
# Process image and predict label
from tensorflow.python.keras.preprocessing.image import image, img_to_array

from static.static_var import IMG_SIZE, MODEL_PATH, CLASS_PATH


# Evaluate the model
def process_predict_image(model_path, class_path, validation_path, image_size):
    """
    Image processing and predicting by operating on the trained model
    :param model_path: Path of trained model
    :param class_path: path of the predictive class
    :param validation_path: Image path that needs to be predicted
    :param image_size: In accordance to the model used for example VGG 224, RESNET-256, NASNET-331 and DENSENET-224
    :return: Predicted labels to be responded with the json
    """
    try:
        # Load the model
        model = tf.keras.models.load_model(model_path)
        # Load classes
        with open(class_path, 'rb') as file:
            # Get a list of categories
            loaded_class = pickle.load(file)
        # Load and reshape the image
        loaded_image = image.load_img(validation_path, target_size=(image_size, image_size))
        input_arr = img_to_array(loaded_image)
        input_arr = np.array([input_arr])
        input_arr = input_arr.astype('float') / 255.0

        # TODO CV2 method can also be used instead of Keras for prediction
        # Prediction using CV2
        # image = cv2.imread(validation_path)
        # # Get input reshaped and rescaled
        # image = cv2.resize(image, (image_size, image_size))
        # image_f = image.astype("float") / 255.0
        # image_a = img_to_array(image_f)
        # image_p = np.expand_dims(image_a, axis=0)
        # # Get predictions
        # predictions = model.predict(image_p).ravel()
        # print (predictions)

        # Get predictions
        predictions = model.predict(input_arr)
        predicted_class = np.argmax(predictions, axis=-1)
        print(predicted_class)
        # Get the class with the highest probability
        prediction = np.argmax(predictions)
        # Check if the prediction is correct
        return loaded_class[prediction]
    except OSError as os:
        # Mismatch file name
        return os.args[0]
    except pickle.UnpicklingError as pe:
        # normal, somewhat expected
        return pe.args[0]
    except (AttributeError, EOFError, ImportError, IndexError) as e:
        # secondary errors
        return e.args[0]
    except Exception as oe:
        # other exceptions
        return oe.args[0]


def processImg(img_validation_path):
    """
    Image processing function
    :param img_validation_path:
    :return: labels of the predicted class
    """
    return process_predict_image(model_path=MODEL_PATH,
                                 class_path=CLASS_PATH,
                                 validation_path=img_validation_path,
                                 image_size=IMG_SIZE)
