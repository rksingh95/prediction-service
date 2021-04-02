# Prediction variables (classifier)
import pymongo

PREDICTION_CLASS = ['barretts',
                    'barretts-short-segment',
                    'bbps-0-1',
                    'bbps-2-3',
                    'cecum',
                    'dyed-lifted-polyps',
                    'dyed-resection-margins',
                    'esophagitis-a',
                    'esophagitis-b-d',
                    'hemorrhoids',
                    'ileum',
                    'impacted-stool',
                    'polyps',
                    'pylorus',
                    'retroflex-rectum',
                    'retroflex-stomach',
                    'ulcerative-colitis-grade-0-1',
                    'ulcerative-colitis-grade-1',
                    'ulcerative-colitis-grade-1-2',
                    'ulcerative-colitis-grade-2',
                    'ulcerative-colitis-grade-2-3',
                    'ulcerative-colitis-grade-3',
                    'z-line',
                    ]
IMG_SIZE = 256
LEARNING_RATE = 0.001
COLOUR_MAP = 3
MODEL_PATH = "models/ResNet2021_23C.h5"
CLASS_PATH = "models/ResNet2021_23C.pkl"

# app.py static var
IMAGE_UPLOAD_PATH = r"C:\Users\Rahul Singh\PycharmProjects\ML_ModelPrediction"
UPLOAD_EXTENSIONS = ['.jpg', '.png', ]
SECRET_KEY = "secret key"

# DB settings
CLIENT = pymongo.MongoClient(
    "mongodb+srv://singh:CMrdUjEgM2iPZGh@cluster0.waaxg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
DB = CLIENT["Endoscopic_Guidance"]
COLUMNS = DB["images"]

# APP SETTINGS
POST_METHOD = ['POST']
GET_METHOD = ['GET']
