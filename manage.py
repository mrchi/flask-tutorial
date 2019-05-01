#!/usr/bin/env python3
# coding=utf-8

import os

from flask.cli import with_appcontext

from flaskr import create_app
from flaskr.models import init_db


config_name = os.environ.get('FLASK_ENV') or 'default'
app = create_app(config_name)


@app.cli.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    app.logger.info('Initialized the database.')
