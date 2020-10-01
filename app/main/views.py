from flask import render_template
from . import main
from flask import Flask,render_template
from flask_material import Material
from flask_googlemaps import GoogleMaps

# views

@main.route('/')
def index():
	return 'Hello World Map With Flask'

@main.route('/map/<string:place>',methods=['GET'])
def map(place):
	return render_template('geo.html',place=place)
