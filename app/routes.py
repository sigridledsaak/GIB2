from flask import render_template, request
from app import app
from .models import Event

@app.route('/index')
def index():
    return "Hello, World!"



@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    date = request.form.get('date')
    category = request.form.get('category')
    ageLimit = request.form.get('ageLimit')
    distance = request.form.get('distance')
    events = Event.query.filter_by(startdate='date')
    print(date)

    #if ageLimit:
        #events = events.remove(Event.query.filter_by(ageLimit='ageLimit').all())
    #if category:
        #events = events.remove(Event.query.filter_by(category='category').all())

    return render_template('home.html', categories= Event.CATEGORY_CHOICES)

#@app.route('/home/search', methods=['GET', 'POST'])
#def searchEvents():




@app.route('/about')
def about():
    return render_template('about.html', title ='About')

@app.route('/register')
def register():
    return render_template('register.html', categories=Event.CATEGORY_CHOICES, title="Register Event")

