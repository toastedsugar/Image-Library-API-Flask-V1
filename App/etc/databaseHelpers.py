import sys, sqlite3
from flask import g
sys.path.append('/Users/ewaste/Documents/Programming/Image-Library-API-Flask-V1/App') 
# from routes.ImagesRoutes import ImgRoutes

DATABASE = './images.db'

def get_db():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    return cursor

def view_all_db():
    all = get_db().execute('SELECT * FROM ImgLibrary').fetchall()
    print(all, flush=True)


# # Open connection to DB
# def get_db():
#     # db = getattr(g, '_database', None)
#     # if db is None:
#     #     db = g._database = sqlite3.connect(DATABASE)
#     # db.row_factory = sqlite3.Row
#     # return db
#     db = sqlite3.connect(DATABASE)
#     db.row_factory = sqlite3.Row
#     return db
    

# # Close db
# # @ImgRoutes.teardown_appcontext
# # def close_connection(exception):
# #     db = getattr(g, '_database', None)
# #     if db is not None:
# #         db.close()

# # Query function that combines getting cursor, performing query and fetching results
# def query_db(query, args=(), one=False):
#     cur = get_db().execute(query, args)
#     rv = cur.fetchall()
#     print(rv, flush=True)
#     cur.close()
#     return (rv[0] if rv else None) if one else rv

