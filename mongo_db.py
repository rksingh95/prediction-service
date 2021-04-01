import datetime
import io
import json
from typing import Dict

import gridfs
import pymongo as pymongo
from PIL import Image

# client = pymongo.MongoClient("mongodb+srv://singh:<CMrdUjEgM2iPZGh>@cluster0.waaxg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# # database connection
# db = client["Endoscopic_Guidance"]


client = pymongo.MongoClient(
    "mongodb+srv://singh:CMrdUjEgM2iPZGh@cluster0.waaxg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client["Endoscopic_Guidance"]


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
    :param file: byte array of loaded image file
    :return: None
    """
    prediction = db.images

    # mongodb server
    imgByteArr = convert_image_to_byte_array(file=file, label=label)
    # database creation
    image_id = prediction.insert_one(imgByteArr).inserted_id
    print(image_id, 'Successfully inserted')


def get_prediction_data():
    """
    Gets the data from the database
    :return:
    """
    col = db["images"]
    x = col.find()
    fetched_data = []
    for data in x:
        data.pop('_id')
        data.pop('data')
        fetched_data.append(data)
    return json.dumps(fetched_data)
