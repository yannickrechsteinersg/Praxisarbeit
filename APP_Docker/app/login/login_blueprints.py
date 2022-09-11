from flask import Blueprint, render_template, url_for
from flask_login import login_required, login_user, logout_user
from werkzeug.utils import redirect

from app import bcrypt
from app.models import LoginForm, User

login_blueprints = Blueprint('login_blueprints', __name__)


@login_blueprints.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect('/dashboard')
    return render_template('login.html', form=form)


@login_blueprints.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect('/login')
