from flask import Flask

UPLOAD_FOLDER = r'C:\Users\Rahul Singh\PycharmProjects\ML_ModelPrediction'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', ]
