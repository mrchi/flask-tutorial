# coding=utf-8

from datetime import datetime

import pytest

from flaskr import create_app
from flaskr.models import init_db, db, User, Post


@pytest.fixture
def app():
    app = create_app('testing')

    # push app context
    app_context = app.app_context()
    app_context.push()

    # initial database
    init_db()
    db.session.add_all([
        User(id=1, username='user1', password='test1'),
        User(id=2, username='user2', password='test2'),
        Post(
            id=1, title='test title', body='test body', author_id=1,
            created=datetime(2019, 1, 1, 0, 0, 1),
        ),
    ])
    db.session.commit()

    yield app

    # clean
    db.session.remove()
    db.drop_all()
    app_context.pop()


@pytest.fixture
def client(app):
    return app.test_client(use_cookies=True)


@pytest.fixture
def cli_runner(app):
    return app.test_cli_runner()


class AuthActions(object):
    def __init__(self, client):
        self._client = client

    def login(self, username='user1', password='test1', url='/auth/login'):
        return self._client.post(
            url, data={'username': username, 'password': password},
        )

    def logout(self):
        return self._client.get('/auth/logout')


@pytest.fixture
def auth(client):
    return AuthActions(client)
