# -*- encoding: utf-8 -*-
# Author: Epix
import os
import uuid

from PIL import Image, ImageDraw
from flask import Flask, send_file, send_from_directory, request, jsonify
from werkzeug.routing import FloatConverter
import tempfile
from make_mosainic import make_mosainic

app = Flask(__name__)
CACHE_PATH = 'cache'
TEMP_PATH = 'temp'


@app.route('/make', methods=['POST'])
def make():
    upload_files = request.files.values()
    temp_input = []
    output_filename = os.path.join(CACHE_PATH, uuid.uuid4().hex + '.jpg')
    for upload_file in upload_files:
        temp_file = tempfile.mkstemp(dir=TEMP_PATH)[1]
        upload_file.save(temp_file)
        temp_input.append(temp_file)
    height, width = make_mosainic(temp_input, output_filename)
    return jsonify({'file': output_filename, 'height': height, 'width': width})


@app.route('/', methods=['GET'])
def homepage():
    return send_from_directory('static', 'index.html')


@app.route('/<path:path>')
def send_static(path):
    return send_from_directory('static', path)


@app.route('/cache/<path:path>')
def send_result(path):
    return send_from_directory('cache', path)


if __name__ == '__main__':
    app.run(
        # debug=True
    )
