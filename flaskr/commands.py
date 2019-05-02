# coding=utf-8

import click
from flask.cli import with_appcontext

from flaskr.models import init_db


@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Initialized the database.')
