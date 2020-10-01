import os
from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from .forms import AddPostForm
from datetime import datetime
from .. import db,photos
from app.models import Case,User,Role,Status

# views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    cases = Case.query.order_by(Case.category)
    return render_template('index.html',cases=cases)

@main.route("/Add/case/",methods = ["GET","POST"])
def case():
    form = AddPostForm()
    title = "Add Post"
    if form.validate_on_submit():
        category = form.category.data
        title = form.title.data
        description = form.description.data
        geolocation = form.geolocation.data

        if "photo" in request.files:
            pic = photos.save(request.files["photo"])
            file_path = f"photos/{pic}"
            image = file_path
        post = Case(category = category, title = title, description=description, geolocation=geolocation, image = image,)
        db.session.add(post)
        db.session.commit()
        
        
    return render_template("add_incidences.html",form = form,title = title)

@main.route('/map/<string:place>',methods=['GET','POST'])
def map(place):

    return render_template('add_incidence.html',place=place)