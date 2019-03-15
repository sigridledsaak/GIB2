from flask import render_template
from app import app
from .models import Event
import requests

@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html', title ='About')

@app.route('/register')
def register():
    return render_template('register.html',title='Register Event')

