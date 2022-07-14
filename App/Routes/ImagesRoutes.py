import os, sqlite3
from re import T
from fileinput import filename
from flask import Blueprint, render_template, abort, request, send_file, flash, g
from jinja2 import TemplateNotFound
from werkzeug.utils import secure_filename

import etc.databaseHelpers as dbHelper

ImgRoutes = Blueprint('ImgRoutes', __name__, template_folder='../templates')

URL = "/v1/static/images"
UPLOAD_FOLDER = 'static/img'
ALLOWED_EXTENSIONS = {'jpg', 'png', 'webp'}

DATABASE = './images.db'

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

    # Check for duplicate files
    for root, dirs, files in os.walk(UPLOAD_FOLDER):
        if newFile.filename in files:
            #return os.path.join(root, name)
            return 'This is a duplicate file'

    # Save file
    if newFile and allowed_file(newFile.filename):
        filename = secure_filename(newFile.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)

        # Insert file into database
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        cursor.execute('INSERT INTO ImgLibrary (name, path) VALUES (?, ?)', 
                                    (filename, filepath))
        db.commit()
        # insertion = cursor.execute('SELECT ? FROM ImgLibrary', (filename,)).fetchall()
        # print(insertion, flush=True)

        allIMG = dbHelper.view_all_db()

        #print('Adding to db: ', allIMG, flush=True)

        # Save image to filesystem
        newFile.save(filepath)
        return 'Success!'
    return 'Failed!'

    


# Delete request to delete an image from the database


# Error handlers here
