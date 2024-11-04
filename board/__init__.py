#from flask import Flask
#from board import pages, database
#import os

#def create_app():
#    app = Flask(__name__)
#    app.config['DATABASE'] = os.path.join(os.getcwd(), 'data', 'board.sqlite')

#    app.config['DEBUG'] = True

#    database.init_app(app)
#    app.register_blueprint(pages.bp)

#    return app
from flask import Flask
from .database import init_app

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        DATABASE='/home/3323600013_Izzah/flask_board/database.db',
    )

    # Register your database functions
    init_app(app)

    # Register blueprints, if any
    from . import pages
    app.register_blueprint(pages.bp)

    return app
