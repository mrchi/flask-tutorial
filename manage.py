#!/usr/bin/env python3
# coding=utf-8

from flaskr import create_app
from flaskr.models import db, Post, User


app = create_app('development')


@app.shell_context_processor
def add_shell_context():
    return dict(db=db, Post=Post, User=User)
