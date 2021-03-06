import os

from flask import Flask


def create_app():
    app = Flask(__name__)

    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    from src.api.text import ocr_blueprint

    app.register_blueprint(ocr_blueprint)

    return app
