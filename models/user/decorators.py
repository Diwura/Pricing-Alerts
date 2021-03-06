import functools
from subprocess import call
from typing import Callable
from flask import session, flash, redirect, url_for, current_app

def requires_login(f:callable) ->  Callable:
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('email'):
            flash("You need to be signed in to continue on this page", 'danger')
            return redirect(url_for('users.login_user'))
        return f(*args, **kwargs)
    return decorated_function

def requires_admin(f:callable) ->  Callable:
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('email') == current_app.config.get('ADMIN',''):
            flash('You need to be an administrator to continue on this page', 'danger')
            return redirect(url_for('users.login_user'))
            return f(*args, **kwargs)
        return decorated_function 