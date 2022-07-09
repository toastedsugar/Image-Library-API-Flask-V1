from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

ImgRoutes = Blueprint('ImgRoutes', __name__, template_folder='../Views')

@ImgRoutes.route('/')
def hello():
    try:
        return "<h1>Hello</h1>"
    except TemplateNotFound:
        abort(404)