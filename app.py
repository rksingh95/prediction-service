from flask import Flask

from static.static_var import IMAGE_UPLOAD_PATH, UPLOAD_EXTENSIONS, SECRET_KEY

app = Flask(__name__)

app.secret_key = SECRET_KEY
app.config['UPLOAD_FOLDER'] = IMAGE_UPLOAD_PATH
app.config['UPLOAD_EXTENSIONS'] = UPLOAD_EXTENSIONS
