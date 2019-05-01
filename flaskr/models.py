# coding=utf-8

from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash

from . import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author_id = db.Column(db.Integer, db.ForeignKey(User.id))
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    title = db.Column(db.String(64), nullable=False)
    body = db.Column(db.Text, nullable=False)


def init_db():
    db.drop_all()
    db.create_all()
