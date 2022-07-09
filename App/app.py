from flask import Flask
from Routes.Images import ImgRoutes

app = Flask(__name__)
app.run(debug=True)

app.register_blueprint(ImgRoutes)