# coding=utf-8

import pytest

from flaskr.models import User, Post


def test_init_db_command(cli_runner, monkeypatch):
    class Recorder(object):
        called = False

    def fake_init_db():
        Recorder.called = True

    monkeypatch.setattr('flaskr.commands.init_db', fake_init_db)
    result = cli_runner.invoke(args=['init-db'])
    assert 'Initialized' in result.output
    assert Recorder.called


def test_fake_command(cli_runner):
    pytest.importorskip("faker")
    user_count = User.query.count()
    post_count = Post.query.count()
    result = cli_runner.invoke(args=['fake'])
    assert 'Generated' in result.output
    assert User.query.count() == user_count + 5
    assert Post.query.count() == post_count + 20
