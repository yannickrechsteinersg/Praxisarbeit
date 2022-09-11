from flask import Blueprint, render_template
from flask_login import login_required
from werkzeug.utils import redirect

from app import db
from app.models import AddressForm, Adress

dashboard_blueprints = Blueprint('dashboard_blueprints', __name__)


@dashboard_blueprints.route('/dashboard', methods=['GET', 'POST'])
def dashboard():

    form = AddressForm()

    if form.validate_on_submit():
        new_user = Adress(name=form.name.data, surname=form.surname.data, street=form.street.data, city=form.city.data, plz=form.plz.data, phonenumber=form.phonenumber.data, country=form.country.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/')

    return render_template('dashboard.html', form=form)
