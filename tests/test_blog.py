# coding=utf-8

import pytest

from flask import url_for

from flaskr.models import Post


def test_index(client, auth):
    resp = client.get('/')
    assert resp.status_code == 200

    data = resp.get_data(as_text=True)
    assert 'test title' in data
    assert 'test body' in data
    assert 'by user1 on 2019-01-01' in data
    assert 'Log In' in data
    assert 'Register' in data
    assert 'href="/1/update"' not in data

    auth.login()
    resp = client.get('/')
    data = resp.get_data(as_text=True)
    assert 'Log Out' in data
    assert 'href="/1/update"' in data


@pytest.mark.parametrize('path', ('/create', '/1/update', '/1/delete'))
def test_login_required(client, path):
    response = client.post(path)
    assert response.headers['Location'] == url_for('auth.login', next=path)


def test_author_required(client, auth):
    auth.login('user2', 'test2')
    assert client.post('/1/update').status_code == 403
    assert client.post('/1/delete').status_code == 403
    assert 'href="/1/update"' not in client.get('/').get_data(as_text=True)


def test_exists_required(client, auth):
    auth.login()
    assert client.post('/2/update').status_code == 404
    assert client.post('/2/delete').status_code == 404


def test_create(client, auth):
    auth.login()
    assert client.get('/create').status_code == 200

    resp = client.post('/create', data={'title': 'created', 'body': ''})
    assert resp.headers['Location'] == url_for('blog.index')

    p = Post.query.filter_by(title='created').first()
    assert p is not None
    assert p.body == ''


def test_update(client, auth):
    auth.login()
    assert client.get('/1/update').status_code == 200

    resp = client.post('/1/update', data={'title': 'updated', 'body': ''})
    assert resp.headers['Location'] == url_for('blog.index')

    p = Post.query.get(1)
    assert p.title == 'updated'
    assert p.body == ''


@pytest.mark.parametrize('path', ('/create', '/1/update'))
def test_title_required_validation(client, auth, path):
    auth.login()
    resp = client.post(path, data={'title': '', 'body': ''})
    assert 'Title is required' in resp.get_data(as_text=True)


def test_delete(client, auth):
    auth.login()
    resp = client.post('/1/delete')
    assert resp.headers['Location'] == url_for('blog.index')
    assert not Post.query.get(1)
