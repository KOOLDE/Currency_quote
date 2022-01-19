from flask import Flask

from . import quote

def create_app():
    # Create and configure the app
    app = Flask(__name__)

    # Register blueprint
    app.register_blueprint(quote.bp)
    app.add_url_rule('/', endpoint='index')

    return app