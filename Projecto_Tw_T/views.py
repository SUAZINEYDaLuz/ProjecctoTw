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
    print(data)
    return render_template("Homepage.html", minhatab=data, user=current_user)


@views.route('/sell')
@login_required
def SellPage():
    return render_template("SellPage.html", user = current_user)

def save_images(image1):
    hash_image1 = secrets.token_urlsafe(10)
    _, file_extention=os.path.splitext(image1.filename)
    image1_name = hash_image1+file_extention
    file_path = os.path.join(current_app.root_path, 'static/images', image1_name)
    image1.save(file_path)
    return image1_name





@views.route('/sell/', methods=['POST'])
@login_required
def Send_Data():
    if request.method == 'POST':
        titlu = request.form['titlu']
        categoria = request.form['categoria']
        descricao = request.form['descricao']
        email = request.form['email']
        image = save_images(request.files.get('image1'))
        lance = request.form['Lance']
        datalance = request.form['dataLeilao']
        new_item = tabelatw(titlu=titlu, categoria=categoria, descricao=descricao, email=email,image=image,lance=lance ,datalance = datalance)
        db.session.add(new_item)
        db.session.commit()
    return render_template('Homepage.html')


@views.route('/autionpage/', methods=['POST', 'GET'])
@login_required
def Auction():
    data = tabelatw.query.all()
    user = tabelalogin.query.all()
    return render_template("AuctionPage.html", user=user, minhatab=data)
def lista():
    pass
