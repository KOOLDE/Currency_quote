from flask import Blueprint
from flask import render_template

from . import api_quote

bp = Blueprint('quote', __name__)

@bp.route('/')
def index():
    datas = api_quote.data
    return render_template('quote/index.html', data=datas)