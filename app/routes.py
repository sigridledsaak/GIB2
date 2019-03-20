import datetime as dt
from flask import render_template, request
from app import app, db
from .models import Event

@app.route('/index')
def index():
    return "Hello, World!"



@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        date = request.form.get('date')
        time = request.form.get('time')
        category = request.form.get('category')
        ageLimit = request.form.get('ageLimit')
        distance = request.form.get('distance')
        events = db.session.query(Event.title, Event.category_name, Event.venueCoordinates, Event.startdate,
                                  Event.ageRestriction).all()
        #print(events)
        if date and time:
            date = dt.datetime.strptime(date, "%Y-%m-%d").date()
            time = dt.datetime.strptime(time, "%H:%M").time()
            datetime = dt.datetime.combine(date, time)
            events = events & db.session.query(Event.title, Event.category_name, Event.venueCoordinates, Event.startdate,
                                  Event.ageRestriction).filter_by(startdate=datetime).all()
        print("passed if")
        print(events)
        """
        if ageLimit:
            events = events.remove(Event.query.filter_by(ageRestriction='ageLimit').all())
        if category:
            events = events.remove(Event.query.filter_by(category='category').all())
        """
        return render_template('home.html', categories= Event.CATEGORY_CHOICES, events=events)
    return render_template('home.html', categories= Event.CATEGORY_CHOICES)

#@app.route('/home/search', methods=['GET', 'POST'])
#def searchEvents():




@app.route('/about')
def about():
    return render_template('about.html', title ='About')

@app.route('/register')
def register():
    return render_template('register.html', categories=Event.CATEGORY_CHOICES, title="Register Event")

