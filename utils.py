import json
import os

from app import app


def invalid_file_error_response(data) -> json:
    data = {"detail_error": 'File format not supported only supported are .jpeg and .png but received a' + ' ' + data}
    response = app.response_class(
        response=json.dumps(data),
        status=400,
        mimetype='application/json'
    )
    return response


def valid_error_response(label) -> json:
    # flash({"Given class of image is ": label})
    data = {"Given a class of image is ": label}
    response = app.response_class(
        response=json.dumps(data),
        mimetype='application/json'
    )
    return response


def invalid_error_response(data) -> json:
    data = {"detail_error": 'No file uploaded' + ' ' + data}
    response = app.response_class(
        response=json.dumps(data),
        status=400,
        mimetype='application/json'
    )
    return response


def invalid_model_path_response(data) -> json:
    data = {"detail_error": 'Application can not find the trained as' + ' ' + data}
    response = app.response_class(
        response=json.dumps(data),
        status=400,
        mimetype='application/json'
    )
    return response


def invalid_method_response() -> json:
    data = {"detail_error": "requested method service is not supported by the application"}
    response = app.response_class(
        response=json.dumps(data),
        status=400,
        mimetype='application/json'
    )
    return response


def remove_img(path, img_name) -> json:
    os.remove(path + '/' + img_name)
    # check if file exists or not
    if os.path.exists(path + '/' + img_name) is False:
        # file did not exists
        return True
