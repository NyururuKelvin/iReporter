import os
from flask import render_template,request
from . import main
from .forms import AddPostForm
from datetime import datetime
from .. import db,photos
from app.models import Case

# views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('display.html')

@main.route("/add/post/",methods = ["GET","POST"])
def case():
    form = AddPostForm()
    title = "Add Post"
    if form.validate_on_submit():
        category = form.category.data
        title = form.title.data
        content = form.content.data
        posted = str(datetime.now())
        print(posted)
        if "photo" in request.files:
            pic = photos.save(request.files["photo"])
            file_path = f"photos/{pic}"
            image = file_path
        case = Case(category = category, title = title,image = image)
        db.session.add(case)
        db.session.commit()
        
        
    return render_template("add_incidences.html",form = form,title = title)

@main.route('/map/<string:place>',methods=['GET','POST'])
def map(place):

    return render_template('add_incidence.html',place=place)