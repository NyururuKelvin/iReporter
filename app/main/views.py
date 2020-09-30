from flask import render_template
from . import main

# views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('admin_incidences.html')

@main.route('/<uname>/blog',methods = ['GET','POST'])
def flag(uname):
    user = User.query.filter_by(username = uname).first()
    form = PostForm()

    if not user.is_authenticated:
        flash('please login', 'danger')
        return redirect(url_for('main.login'))
   
    if form.validate_on_submit():
        category = form.category.data
        title = form.title.data
        description = form.description.data
        image = form.image.data
        video = form.video.data
        location = form.location.data
        
        post = Post(owner_id=user.id, category=category, title=title, description=description, image=image, video=video, location=location)
        db.session.add(flag)
        db.session.commit()

        flash('your Red Flag has been added successfuly!', 'success')
        return redirect(url_for('main.index',uname=user.username))

    return render_template('dashboard.html', uname=user.username ,form =form)