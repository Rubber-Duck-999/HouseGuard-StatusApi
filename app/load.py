from flask import Flask
from app import routes

def create_app():

    app = Flask(__name__, static_url_path='', template_folder="static/pages")
    register_blueprints(app)

    return app

def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(routes.api.api_bp)

    return None