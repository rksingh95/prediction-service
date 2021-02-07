import json
import os

from app import app
from flask import render_template, request
from werkzeug.utils import secure_filename

from classifier import getPrediction



@app.route('/')
def index():
    return render_template('about.html')


@app.route('/upload-image/', methods=['POST'])
def submit_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            data = "File not found in request body"
            response = app.response_class(
                response=json.dumps(data),
                mimetype='application/json'
            )
            # flash('No file part')
            # return redirect(request.url)
            return response
        file = request.files['file']
        if file.filename == '':
            data = 'No file selected for uploading'
            response = app.response_class(
                response=json.dumps(data),
                mimetype='application/json'
            )
            # flash('No file selected for uploading')
            # return redirect(request.url)
            return response
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # upload images to DB
            # upload_image_data_mongodb(file)
            label = getPrediction.processImg(filename)
            # flash({"Given class of image is ": label})
            data = {"Given class of image is ": label}
            response = app.response_class(
                response=json.dumps(data),
                mimetype='application/json'
            )
            if remove_img(path=os.path.join(app.config['UPLOAD_FOLDER']), img_name=file.filename):
                print('Image removed')
            # return redirect('/')
            return response


def remove_img(path, img_name):
    os.remove(path + '/' + img_name)
    # check if file exists or not
    if os.path.exists(path + '/' + img_name) is False:
        # file did not exists
        return True


if __name__ == "__main__":
    app.run()
