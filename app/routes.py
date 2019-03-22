import datetime as dt
from flask import render_template, request
from sqlalchemy import or_, and_
from app import app, db
from .models import Event
from shapely import wkb


@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():

    def convertCoordinates(hexlocation):
        point = wkb.loads(hexlocation, hex=True)
        longitude = point.x
        latitude = point.y
        return [longitude, latitude]

    if request.method == 'POST':
        #Get user input
        date = request.form.get('date')
        time = request.form.get('time')
        category = request.form.get('category')
        ticketPrize = request.form.get('ticketPrize')
        ageLimit = request.form.get('ageLimit')
        distance = request.form.get('distance')

        filters = []

        if date and time:
            date = dt.datetime.strptime(date, "%Y-%m-%d").date()
            time = dt.datetime.strptime(time, "%H:%M").time()
            datetime = dt.datetime.combine(date, time)
            delta = datetime + dt.timedelta(days=1)
            filters.append(Event.startdate >= datetime)
            filters.append(Event.startdate <= delta)
        if ageLimit:
            filters.append(or_(Event.ageRestriction < ageLimit, Event.ageRestriction == None))
        if category:
            filters.append(Event.category_name == category)
        if ticketPrize:
            filters.append(Event.regularPrice < ticketPrize)

        events = db.session.query(Event.title, Event.ageRestriction, Event.category_name, Event.startdate, Event.venueCoordinates)\
            .filter(and_(*filters)).all()

        """
        for event in events:
            event.venueCoordinates = convertCoordinates(str(event.venueCoordinates))
        """
        return render_template('home.html', categories=Event.CATEGORY_CHOICES, events=events)
    return render_template('home.html', categories=Event.CATEGORY_CHOICES)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register')
def register():
    return render_template('register.html', categories=Event.CATEGORY_CHOICES, title="Register Event")
