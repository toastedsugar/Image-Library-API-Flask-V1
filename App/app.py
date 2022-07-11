from unicodedata import name
from flask import Flask, render_template
from routes.ImagesRoutes import ImgRoutes

app = Flask(__name__)
app.run(debug=True)

app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000

app.register_blueprint(ImgRoutes)

# Default index page
@app.route('/')
def defaultIndex():
    return render_template('index.html', name=name)