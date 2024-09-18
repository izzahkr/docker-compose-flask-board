from flask import Flask
from board import pages, database

def create_app():
    app = Flask(__name__)
    app.config['DATABASE'] = 'board.sqlite'

    database.init_app(app)
    app.register_blueprint(pages.bp)

    return app
