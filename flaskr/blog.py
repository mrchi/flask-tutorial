# coding=utf-8

from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

from .models import Post, User, db


bp = Blueprint('blog', __name__)


@bp.route('/', endpoint='index')
def index():
    posts = Post.query.all()
    return render_template('blog/index.html', posts=posts)


@bp.route('/create', methods=['GET', 'POST'], endpoint='create')
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if not error:
            post = Post(title=title, body=body, author_id=current_user.id)
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('blog.index'))
        else:
            flash(error)

    return render_template('blog/create.html')


@bp.route('/<int:id>/update', methods=['GET', 'POST'], endpoint='update')
def update(id):
    return 'update page'
