import os, databaseHelpers

UPLOAD_FOLDER = 'static/img'

# Initialize database
def init_db():
    # delete old database
    DBpath = '../images.db'
    if os.path.exists(databaseHelpers.DATABASE):
        print('Deleting old database', flush=True)
        os.remove(databaseHelpers.DATABASE)
    else:
        print('No db found', flush=True)
    
    # Delete all images
    for file in os.scandir(UPLOAD_FOLDER):
        os.remove(file.path)
        print('Removing ', file.path, flush=True)

    cursor = databaseHelpers.get_db().cursor()
    cursor.execute("CREATE TABLE ImgLibrary (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, path TEXT NOT NULL)")
    print('Initializing db: ', databaseHelpers.query_db('SELECT name FROM sqlite_master WHERE type = "table"'), flush=True)

init_db()