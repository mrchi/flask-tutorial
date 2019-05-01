# coding=utf-8

import pytest

from flask import url_for
from flask_login import current_user

from flaskr.models import User


@pytest.mark.parametrize(
    ('username', 'password', 'message'),
    (
        ('', '', 'Username is required'),
        ('user', '', 'Password is required.'),
        ('user1', 'password', 'User user1 is already registered'),
    ),
)
def test_register_validation(client, username, password, message):
    resp = client.post(
        '/auth/register',
        data={'username': username, 'password': password},
        follow_redirects=True,
    )
    assert message in resp.get_data(as_text=True)


def test_register(client):
    assert client.get('/auth/register').status_code == 200
    resp = client.post(
        '/auth/register', data={'username': 'a', 'password': 'a'},
    )
    assert resp.headers['Location'] == url_for('auth.login')
    u = User.query.filter_by(username='a').first()
    assert u
    assert u.verify_password('a')


@pytest.mark.parametrize(
    ('username', 'password', 'message'),
    (
        ('user_not_exist', 'test123', 'Incorrect username or password'),
        ('user1', 'wrong_password', 'Incorrect username or password'),
    ),
)
def test_login_validation(auth, username, password, message):
    resp = auth.login(username, password)
    assert message in resp.get_data(as_text=True)


def test_login_logout(auth, client):
    assert client.get('/auth/login').status_code == 200
    resp = auth.login(url='/auth/login?next=%2F1%2Fupdate')
    assert resp.headers['Location'] == url_for('blog.update', post_id=1)

    # Using client in a with block allows accessing context variables
    with client:
        client.get('/')
        assert current_user.is_authenticated
        assert current_user.username == 'user1'

    resp = auth.logout()
    assert resp.status_code == 302

    with client:
        client.get('/')
        assert not current_user.is_authenticated
