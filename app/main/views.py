from . import main
from flask_login import current_user, login_required
from .forms import AddPostForm,SubscribeForm,AddComment,EditBio
from ..models import Post,User,Comment,Subscriber
from flask import render_template
from . import main
from flask import Flask,render_template
from flask_material import Material
from flask_googlemaps import GoogleMaps
@main.route("/", methods = ["GET","POST"])
def index():
    form = SubscribeForm()
    if form.validate_on_submit():
        email = form.email.data
        new_subscriber = Subscriber(email = email)
        db.session.add(new_subscriber)
        db.session.commit()
        flash("Thank You for subscribing!")
        return redirect(url_for("main.index"))
    posts = Post.query.order_by(Post.time.desc())
    title = "Home"
    return render_template("index.html",posts = posts,form = form,title = title)

@main.route("/add/post/",methods = ["GET","POST"])
@login_required
def add_post():
    form = AddPostForm()
    title = "Add Post"


    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        posted = str(datetime.now())
        print(posted)
        if "photo" in request.files:
            pic = photos.save(request.files["photo"])
            file_path = f"photos/{pic}"
            image = file_path
        new_post = Post(title = title, content = content, user = current_user,image = image,time = posted)
        new_post.save_post()
        subscribers = Subscriber.query.all()
        emails = []
        for subscriber in subscribers:
            emails.append(subscriber.email)
        for email in emails:
            create_mail("Update!","email/update",email, user = current_user)
        print(emails)
        return redirect(url_for('main.index'))

    return render_template("add_pitch.html",form = form,title = title)

@main.route('/')
def index():
	return 'Hello World Map With Flask'

@main.route('/map/<string:place>',methods=['GET'])
def map(place):
	return render_template('geo.html',place=place)
