# coding=utf-8

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from config import config

db = SQLAlchemy()
migrate = Migrate(db=db)
login_manager = LoginManager()
login_manager.login_view = 'auth.login'


def create_app(config_name=None):
    app = Flask(__name__)
    config_name = config_name or os.environ.get('FLASK_ENV') or 'default'
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    migrate.init_app(app)
    login_manager.init_app(app)

    from flaskr.views import auth, blog
    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)

    from flaskr.commands import init_db_command, generate_fake_data
    app.cli.add_command(init_db_command)
    app.cli.add_command(generate_fake_data)

    return app
