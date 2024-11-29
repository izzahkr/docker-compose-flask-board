from flask import Flask
from .database import init_app

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        DATABASE='/home/3323600013_Izzah/flask_board/database.py',
    )

    # Initialize the database
    init_app(app)

    # Register blueprints
    from . import pages
    app.register_blueprint(pages.bp)

    return app
