import os

from app import app
from flask import render_template, request, redirect, flash
from werkzeug.utils import secure_filename

from classifier import getPrediction
from mongo_db import upload_image_data_mongodb


@app.route('/')
def index():
    return render_template('about.html')


@app.route('/', methods=['POST'])
def submit_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # upload images to DB
            upload_image_data_mongodb(file)
            label = getPrediction.processImg(filename)
            flash({"Given class of image is ": label})
            if remove_img(path=r"C:\Users\Rahul Singh\PycharmProjects\flaskProject", img_name=file.filename):
                print('Image removed')
            return redirect('/')


def remove_img(path, img_name):
    os.remove(path + '/' + img_name)
    # check if file exists or not
    if os.path.exists(path + '/' + img_name) is False:
        # file did not exists
        return True


if __name__ == "__main__":
    app.run()
