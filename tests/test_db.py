# coding=utf-8

import pytest

from flaskr.models import User, Post


def test_user_password_setter():
    u = User(username='test', password='cat')
    assert u.password_hash is not None


def test_user_password_no_getter():
    u = User(username='test', password='cat')
    with pytest.raises(AttributeError) as e:
        u.password
    assert 'not a readable' in str(e)


def test_user_password_verification():
    u = User(username='test', password='cat')
    assert u.verify_password('cat') is True
    assert u.verify_password('dog') is False


def test_user_password_salt_random():
    u1 = User(username='test1', password='cat')
    u2 = User(username='test2', password='cat')
    assert u1.password_hash != u2.password_hash


def test_model_repr(client):
    u = User.query.get(1)
    assert repr(u) == '<User (1, user1)>'
    p = Post.query.get(1)
    assert repr(p) == '<Post (1, test title)>'
