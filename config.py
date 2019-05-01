# coding=utf-8

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'it is a secret'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI') \
        or 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI') \
        or 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('PROD_DATABASE_URI') \
        or 'sqlite:///' + os.path.join(basedir, 'data-prod.sqlite')


config = {
    'development': DevConfig,
    'testing': TestConfig,
    'production': ProdConfig,
    'default': DevConfig,
}
