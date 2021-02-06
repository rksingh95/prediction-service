import io
import pymongo as pymongo
from PIL import Image

myclient = pymongo.MongoClient(
    "mongo_uri")
# database creation
db = myclient["Endoscopic_Guidance"]


def convert_image_to_byte_array(file):
    im = Image.open(file)
    image_bytes = io.BytesIO()
    im.save(image_bytes, format='JPEG')
    image = {
        'data': image_bytes.getvalue()
    }
    return image


def upload_image_data_mongodb(file):
    images = db.images
    # mongodb server
    imgByteArr = convert_image_to_byte_array(file=file)
    # database creation
    image_id = images.insert_one(imgByteArr).inserted_id
    print(image_id, 'Successfully inserted')

