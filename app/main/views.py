import os
from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from .forms import AddPostForm
from datetime import datetime
from .. import db,photos
from app.models import Case,User,Role,Status
from flask_login import login_required

# views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    cases = Case.query.order_by(Case.category)
    return render_template('index.html',cases=cases)

@main.route("/Add/case/",methods = ["GET","POST"])
@login_required
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

@main.route('/dashboard')
def dashboard():

    '''
    View root page function that returns the dashboard page and its data
    '''

    return render_template('dashboard.html')

@main.route("/post/<int:id>",methods = ["GET","POST"])
def post_page(id):
    post = Case.query.filter_by(id = id).first()
    title = post.title
    form = AddComment()
    if form.validate_on_submit():
        name = form.name.data
        content = form.comment.data
        new_comment = Comment(name = name, content = content, post = post)
        new_comment.save_comment()
        return redirect(url_for('main.post_page', id = post.id))
    comments = Comment.query.filter_by(post_id = post.id)
    title = post.title
    return render_template("display.html", title = title, post = post,form = form,comments = comments)