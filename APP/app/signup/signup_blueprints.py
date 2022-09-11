from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect

from app import bcrypt, db
from app.models import RegisterForm, User

signup_blueprints = Blueprint('signup_blueprints', __name__)


@signup_blueprints.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/login')

    return render_template('register.html', form=form)