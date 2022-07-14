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

    # cursor = databaseHelpers.get_db().cursor()

    cursor = databaseHelpers.get_db()
    cursor.execute("CREATE TABLE ImgLibrary (name TEXT NOT NULL, path TEXT NOT NULL)")
    newDB_name = cursor.execute('SELECT name FROM sqlite_master WHERE type = "table"').fetchall()
    print('Initializing db: ', newDB_name, flush=True)

init_db()