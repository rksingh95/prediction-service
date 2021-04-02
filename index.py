import json
import os

from app import app
from flask import request
from werkzeug.utils import secure_filename

from mongo_db import upload_image_data_mongodb, get_prediction_data
from static.static_var import prediction_classs
from classifier import getPrediction
from utils import valid_error_response, invalid_error_response, invalid_file_error_response, remove_img, \
    invalid_model_path_response


@app.route('/upload-image/', methods=['POST'])
def submit_file() -> json:
    """
    Accepting  payload of the image and then it performs three tasks:
    1. Image prediction using getPrediction.py file (Script)
    2. Error handling using utils.py file (Script)
    3. DB updating using mongo_db.py file (Script)
    :return: valid or invalid responses depending on the requirements
    """

    if request.method == 'POST':
        uploaded_file = request.files.get('', None)
        filename = uploaded_file.filename
        # Validate if file is present
        if not filename:
            return invalid_error_response(filename)
        if filename:
            # Validate file extension (Only accepted are .jpeg and .png)
            file_ext = os.path.splitext(filename)[1]
            if file_ext not in app.config['UPLOAD_EXTENSIONS']:
                return invalid_file_error_response(file_ext)
            filename = secure_filename(filename)
            uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            label = getPrediction.processImg(filename)
            # upload images and prediction to DB
            upload_image_data_mongodb(uploaded_file, label)
            # Remove locally stored file
            remove_img(path=os.path.join(app.config['UPLOAD_FOLDER']), img_name=filename)

            if label in prediction_classs:
                # To make sure that we receive the labels from prediction class
                return valid_error_response(label)
            else:
                return invalid_model_path_response(label)
            # return redirect(PIL'/')


@app.route('/prediction-history/', methods=['GET'])
def get_prediction_history() -> dict:
    """
    Gets all the predictions made till now extracting from the data base
    :return:
    """
    return get_prediction_data()


if __name__ == "__main__":
    app.run()
