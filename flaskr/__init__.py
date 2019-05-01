# coding=utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import config

db = SQLAlchemy()
migrate = Migrate(db=db)


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    migrate.init_app(app)

    @app.route('/hello')
    def hello():
        return 'hello, world'

    return app
