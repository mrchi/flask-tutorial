# coding=utf-8

from flask import Blueprint, render_template, request, redirect, url_for, \
    flash, abort
from flask_login import login_required, current_user

from flaskr.models import Post, db


bp = Blueprint('blog', __name__)


@bp.route('/', endpoint='index')
def index():
    posts = Post.query.order_by(Post.created.desc()).all()
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


@bp.route('/<int:post_id>/update', methods=['GET', 'POST'], endpoint='update')
@login_required
def update(post_id):
    post = Post.query.get(post_id)
    if post is None:
        abort(404, f'Post id {post_id} doesn\'t exists.')
    if post.author_id != current_user.id:
        abort(403)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if not error:
            post.title = title
            post.body = body
            db.session.commit()
            return redirect(url_for('blog.index'))
        else:
            flash(error)

    return render_template('blog/update.html', post=post)


# delete button is a field of form, so here using post
@bp.route('/<int:post_id>/delete', methods=['POST'], endpoint='delete')
@login_required
def delete(post_id):
    post = Post.query.get(post_id)
    if post is None:
        abort(404, f'Post id {post_id} doesn\'t exists.')
    if post.author_id != current_user.id:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('blog.index'))
