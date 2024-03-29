from flask import Flask, request
from flask_restx import Api
from config import Config
from setup_db import db
from views.movies import movie_ns
from views.direcrors import director_ns
from views.genres import genre_ns


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)
    '''create_data(app, db)



def create_data(app, db):
    ...'''

app = create_app(Config())
app.debug = True




if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)



