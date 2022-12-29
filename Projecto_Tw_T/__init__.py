from flask import Flask
from flask import flash, Blueprint, request, render_template, redirect, url_for
from flask_login import login_required, login_user, current_user, logout_user, LoginManager
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()
# db = MySQL()
password = 'Unitelfo123'


def create_app():
    app.config['SECRET_KEY'] = 'TW_EBECU_CU_GABI'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root:{password}@localhost/contacts'
    db.init_app(app)

    from .auth import auth
    from .views import views

    from .models import tabelalogin

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(ID):
        return tabelalogin.query.get(int(ID))

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app