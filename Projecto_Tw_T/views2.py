from flask import flash, Blueprint, request, render_template, redirect, url_for, current_app
from flask_login import login_required, current_user

from .models import tabelalogin, tabelatw
from . import db
import secrets
import os

views = Blueprint('views', __name__)


@views.route('/', methods=['POST', 'GET'])
@login_required
def Homepage():
    data = tabelatw.query.all()
    return render_template("Homepage.html", minhatab=data, user=current_user)


@views.route('/sell')
@login_required
def SellPage():
    return render_template("SellPage.html", user=current_user)


def save_images(image1):
    hash_image1 = secrets.token_urlsafe(10)
    _, file_extention = os.path.splitext(image1.filename)
    image1_name = hash_image1 + file_extention
    file_path = os.path.join(current_app.root_path, 'static/images', image1_name)
    image1.save(file_path)
    return image1_name


def save_update(imageupdate):
    hash_imageupdate = secrets.token_urlsafe(10)
    _, file_extention = os.path.splitext(imageupdate.filename)
    imageupdate_name = hash_imageupdate + file_extention
    file_path = os.path.join(current_app.root_path, 'static/images', imageupdate_name)
    imageupdate.save(file_path)
    return imageupdate_name


@views.route('/sell/', methods=['POST'])
def Send_Data():
    if request.method == 'POST':
        titlu = request.form['titlu']
        categoria = request.form['categoria']
        descricao = request.form['descricao']
        email = request.form['email']
        image = save_images(request.files.get('image1'))
        new_item = tabelatw(titlu=titlu, categoria=categoria, descricao=descricao, email=email, image=image)
        db.session.add(new_item)
        db.session.commit()
    return render_template('Homepage.html', user=current_user)


@views.route('/profile')
@login_required
def profile():
    data = tabelatw.query.all()
    return render_template("profile.html", minhatab=data, user=current_user)


@views.route('/edit', methods=['POST'])
@login_required
def edit():
    if request.method == 'POST':
        data_update = tabelatw.query.get_or_404(request.form['id'])
        return render_template('Update.html', product=data_update)


@views.route('/update', methods=['POST', 'GET'])
def update():
    # form = Send_Data()
    data_update = tabelatw.query.get_or_404(request.form['id'])
    if request.method == "POST":
        data_update.titlu = request.form['titlu']
        data_update.categoria = request.form['categoria']
        data_update.descricao = request.form['descricao']
        data_update.image = save_update(request.files.get('imageupdate'))
        try:
            db.session.commit()
            flash("Date Updated Successfully")
        except:
            flash("Error!!!")
            return redirect('/profile')
    else:
        return redirect('/profile')


@views.route('/delete/<int:id>')
def delete(id):
    data_delete = tabelatw.query.get_or_404(id)
    try:
        db.session.delete(data_delete)
        db.session.commit()
        return redirect('/profile')
    except:
        return "Problem"
