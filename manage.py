#!/usr/bin/env python3
# coding=utf-8

import os

from flaskr import create_app


config_name = os.environ.get('FLASK_ENV') or 'default'
app = create_app(config_name)
