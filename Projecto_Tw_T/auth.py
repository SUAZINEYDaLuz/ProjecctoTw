from flask import flash, Blueprint, request, render_template, redirect, url_for
from .models import tabelalogin
from flask_login import login_required, login_user, logout_user


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = tabelalogin.query.filter_by(email=email).first()
        if user:
            if user.password == password:
                login_user(user, remember=True)
                return redirect(url_for('views.Homepage'))
            else:
                flash("Password incorrect!!", category='error')
                # App.js.document.getElementById('log_pass').style.borderBottom = '1px solid red'
        else:
            flash("Email does not exist!!", category='error')
            # App.js.document.getElementById('log_email').style.borderBottom = '1px solid red'
    return render_template('login.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
