# coding=utf-8

from flask import Blueprint, render_template

from .models import Post, User, db


bp = Blueprint('blog', __name__)


@bp.route('/', endpoint='index')
def index():
    posts = Post.query.all()
    return render_template('blog/index.html', posts=posts)


@bp.route('/create', methods=['GET', 'POST'], endpoint='create')
def create():
    return 'create page'


@bp.route('/<int:id>/update', methods=['GET', 'POST'], endpoint='update')
def update(id):
    return 'update page'
