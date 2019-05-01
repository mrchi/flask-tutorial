# coding=utf-8

from flask import current_app


def test_app_config(app):
    assert current_app.testing is True
    assert current_app.debug is False
