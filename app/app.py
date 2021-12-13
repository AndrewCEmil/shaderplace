import os

from flask import Flask, request, jsonify
from flask import send_from_directory

static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static')
dist_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'dist')
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return send_from_directory(static_file_dir, 'index.html')

@app.route('/index.html', methods=['GET'])
def index():
    return send_from_directory(static_file_dir, 'index.html')

@app.route('/edit.html', methods=['GET'])
def edit():
    return send_from_directory(static_file_dir, 'edit.html')

@app.route('/present.html', methods=['GET'])
def present():
    return send_from_directory(static_file_dir, 'present.html')

# Hack for defaultShaders
@app.route('/defaultShaders.js', methods=['GET'])
def defaultShaders():
    return send_from_directory(static_file_dir, 'defaultShaders.js')



@app.route('/dist/<path:path>', methods=['GET'])
def serve_file_in_dir(path):
        return send_from_directory(dist_file_dir, path)

app.run(host='0.0.0.0',port=8080)
