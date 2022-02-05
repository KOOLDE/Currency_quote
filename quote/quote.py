from flask import Blueprint
from flask import render_template

from . import api_quote

bp = Blueprint('quote', __name__)

@bp.route('/')
def index():
    API_data = api_quote.data_formated
    return render_template('quote/index.html', data=API_data)