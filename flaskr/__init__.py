# coding=utf-8

from flask import Flask

from config import config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    @app.route('/hello')
    def hello():
        return 'hello, world'

    return app
