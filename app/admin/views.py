from flask import render_template
from . import admin


@admin.route('/admin')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('admin/admin.html')