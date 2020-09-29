from flask import render_template
from . import user


@user.route('/user')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('user/user.html')