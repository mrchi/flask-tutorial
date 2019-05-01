# coding=utf-8

from flask import Blueprint, request, redirect, url_for, flash, render_template

from .models import User, db


bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=['GET', 'POST'], endpoint='register')
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif User.query.filter_by(username=username).first():
            error = f'User {username} is already registered.'

        if not error:
            user = User(username=username, password=password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        else:
            flash(error)

    return render_template('auth/register.html')


@bp.route('/login', methods=['GET', 'POST'], endpoint='login')
def login():
    return 'this is the login page.'
