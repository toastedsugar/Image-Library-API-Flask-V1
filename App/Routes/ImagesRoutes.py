import os, sqlite3
from fileinput import filename
from flask import Blueprint, render_template, abort, request, send_file, flash, g
from jinja2 import TemplateNotFound
from werkzeug.utils import secure_filename

ImgRoutes = Blueprint('ImgRoutes', __name__, template_folder='../templates')

URL = "/v1/static/images"
UPLOAD_FOLDER = 'static/img'
ALLOWED_EXTENSIONS = {'jpg', 'png', 'webp'}
DATABASE = '/database.db'

#ImgRoutes.config['UPLOAD_FOLDER'] = 'static/img'

def allowed_file(fileName):
    return '.' in fileName and \
        fileName.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Index Route shows every image in the database
@ImgRoutes.route(URL + '/', methods=['GET'])
def viewIndex():
    try:
        return "<h1>This is an Image</h1>"
    except TemplateNotFound:
        abort(404)

# GET request to view an image
@ImgRoutes.route(URL + "/<imgTitle>", methods=['GET'])
def viewImg(imgTitle):
    try:
        imgPath = "static/img/" + imgTitle + ".jpg"
        return send_file(imgPath, mimetype='image/jpg')
    except TemplateNotFound:
        abort(404)

# POST request to add an image to the database
@ImgRoutes.route(URL, methods=['POST'])
def addImg():
    print(request.files, flush=True)

    #return 'fdafdsfdasfdsffs'
    # Checking if the request has a file
    if 'file' not in request.files:
        flash('No file')
        return render_template('index.html')
    # Create a new file from request
    newFile = request.files['file']
    print(newFile.filename, flush=True)
    # Checking if the file is empty
    if newFile.filename == '':
        print("No selected file", flush=True)
        flash('No selected file')
        return 'Failed!'
    if newFile and allowed_file(newFile.filename):
        filename = secure_filename(newFile.filename)
        newFile.save(os.path.join(UPLOAD_FOLDER, filename))
        return 'Success!'
    return 'Failed!'

    


# Delete request to delete an image from the database


# Error handlers here
