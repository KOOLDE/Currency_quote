from flask import Blueprint
from flask import render_template

bp = Blueprint('quote', __name__)

@bp.route('/')
def index():
    name:str = 'Index Page'
    return render_template('quote/index.html', user=name)