
from . import admin
from flask import render_template,redirect,url_for,request
from flask_login import login_user,logout_user,login_required
from ...models import Admin
from .forms import LoginForm, RegistrationForm
from ... import db
from ...email import mail_message

@admin.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        admin = Admin.query.filter_by(email = login_form.email.data).first()
        if admin is not None and admin.verify_password(login_form.password.data):
            login_user(admin,login_form.remember.data)
    title = "Pitch login"
    return render_template('admin/login.html',form = login_form,title=title,admin=admin)

@admin.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for(".login"))

@admin.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        admin = Admin(email = form.email.data, username = form.username.data, password = form.password.data )
        db.session.add(admin)
        db.session.commit()

        mail_message("Welcome to pitch","email/welcome_user",admin.email,admin=admin)

        return redirect(url_for('.login'))
        title = "New Account"
    return render_template('admin/register.html',form = form)