import datetime
import io
import json
from typing import Dict

from PIL import Image

# Setting up DB connection
from static.static_var import DB, COLUMNS
from utils import db_timeout_error


def convert_image_to_byte_array(file, label) -> Dict[str, bytes]:
    """
    Converts the raw image file to binary file to make it ready for loadable in the DB
    :param label: Predicted label
    :param file: raw image
    :return: byte array of loaded image file
    """
    im = Image.open(file)
    image_bytes = io.BytesIO()
    im.save(image_bytes, format='JPEG')
    dateTimeObj = datetime.datetime.now()
    timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")

    image = {
        'data': image_bytes.getvalue(),
        'file_name': file.filename,
        'predicted_label': label,
        'predicted_time': timestampStr
    }
    return image


def upload_image_data_mongodb(file, label) -> None:
    """
    Uploads the byte array of the image to DB to used for future reference and its prediction value
    :param label: predicted label
    :param file: byte array of loaded image file
    :return: None
    """
    try:
        prediction = DB.images

        # mongodb server
        imgByteArr = convert_image_to_byte_array(file=file, label=label)
        # database creation
        image_id = prediction.insert_one(imgByteArr).inserted_id
        print(image_id, 'Successfully inserted')
    except TimeoutError as te:
        return db_timeout_error(data=te)


def get_prediction_data() -> json:
    """
    Gets the data from the database
    :return:
    """
    x = COLUMNS.find()
    fetched_data = []
    for data in x:
        data.pop('_id')
        data.pop('data')
        fetched_data.append(data)
    return json.dumps(fetched_data)
