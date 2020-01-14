from flask import Flask, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
from get_genre import find as Model
import os

UPLOAD_FOLDER = '../data'
ALLOWED_EXTENSIONS = {'mp3', 'wav'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['POST'])
def get_genre():
        if 'file' not in request.files:
            return jsonify("Sorry, no file was found.")
        
        file = request.files['file']

        if file.filename == '':
            return jsonify("Sorry, no file was sent.")

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            genres = Model(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return jsonify(genres)

if __name__ == '__main__':
    app.run()