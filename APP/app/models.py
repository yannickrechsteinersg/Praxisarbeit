from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError

from app import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)


class Adress(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    surname = db.Column(db.String(80), nullable=False)
    street = db.Column(db.String(80), nullable=False)
    city = db.Column(db.String(80), nullable=False)
    plz = db.Column(db.String(80), nullable=False)
    phonenumber = db.Column(db.String(80), nullable=False)
    country = db.Column(db.String(80), nullable=False)


class RegisterForm(FlaskForm):
    username = StringField(validators=[
        InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
        InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Register')

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        if existing_user_username:
            raise ValidationError(
                'That username already exists. Please choose a different one.')


class LoginForm(FlaskForm):
    username = StringField(validators=[
        InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
        InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')


class AddressForm(FlaskForm):
    name = StringField(validators=[
        InputRequired(), Length(min=2, max=20)], render_kw={"placeholder": "Name"})

    surname = StringField(validators=[
        InputRequired(), Length(min=2, max=20)], render_kw={"placeholder": "Surname"})

    street = StringField(validators=[
        InputRequired(), Length(min=2, max=20)], render_kw={"placeholder": "Street"})

    city = StringField(validators=[
        InputRequired(), Length(min=2, max=20)], render_kw={"placeholder": "City"})

    plz = StringField(validators=[
        InputRequired(), Length(min=2, max=20)], render_kw={"placeholder": "PLZ"})

    phonenumber = StringField(validators=[
        InputRequired(), Length(min=2, max=20)], render_kw={"placeholder": "Phone Number"})

    country = StringField(validators=[
        InputRequired(), Length(min=2, max=20)], render_kw={"placeholder": "Country"})

    submit = SubmitField('Add Record')
