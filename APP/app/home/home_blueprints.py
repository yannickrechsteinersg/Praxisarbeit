from flask import Blueprint, render_template
from app.models import Adress

home_blueprints = Blueprint('home_blueprints', __name__)


@home_blueprints.route('/')
def home():

    data = Adress.query.all()
    return render_template('home.html', data=data)
