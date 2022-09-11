from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__, template_folder='templates')

    app.config.from_object('config.Config')

    from app.dashboard.dashboard_blueprints import dashboard_blueprints
    app.register_blueprint(dashboard_blueprints)

    from app.home.home_blueprints import home_blueprints
    app.register_blueprint(home_blueprints)

    from app.login.login_blueprints import login_blueprints
    app.register_blueprint(login_blueprints)

    from app.signup.signup_blueprints import signup_blueprints
    app.register_blueprint(signup_blueprints)

    login_manager.init_app(app)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.login_view = 'login'

    """
        Database has been initialized and automatically map tables as per models created
    """
    db.init_app(app)
    with app.app_context():
        db.create_all()
        db.session.commit()

    return app
