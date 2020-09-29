from flask import render_template
from . import auth


@auth.route('/register')
def register():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('auth/register.html')