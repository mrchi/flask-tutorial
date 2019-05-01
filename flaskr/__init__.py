# coding=utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from config import config

db = SQLAlchemy()
migrate = Migrate(db=db)
login_manager = LoginManager()
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    migrate.init_app(app)
    login_manager.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    @app.route('/', endpoint='index')
    def index():
        return 'index page.'

    return app
