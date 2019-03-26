from flask import render_template, request
from app import app, db
from .models import Event
from app.forms import EventForm
from geopy.geocoders import Nominatim
import datetime as dt


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

    # if ageLimit:
    # events = events.remove(Event.query.filter_by(ageLimit='ageLimit').all())
    # if category:
    # events = events.remove(Event.query.filter_by(category='category').all())

    return render_template('home.html', categories=Event.CATEGORY_CHOICES)


# @app.route('/home/search', methods=['GET', 'POST'])
# def searchEvents():


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=('POST', 'GET'))
def register():
    # Skal kalles ved submit..
    if request.method == 'POST':

        new_event = create_empytevent()
        addfieldstoemptyevent(new_event)

        #Adding the event to db
        db.session.add(new_event)
        db.session.commit()
        print("Object added!")

    return render_template('register.html', categories=Event.CATEGORY_CHOICES, title="Register Event")


def correctdateTime(startTime, date):
    date = dt.datetime.strptime(date, "%Y-%m-%d").date()
    time = dt.datetime.strptime(startTime, "%H:%M").time()

    return dt.datetime.combine(date, time)

def addfieldstoemptyevent(event):
    event.title = request.form.get('title')
    event.FID = 0
    event.description = request.form.get('description')
    event.venueName = request.form.get('venueName')
    event.venueAddress = request.form.get('venueAddress')
    print('category: ', request.form.get('category'))
    event.category_name = request.form.get('category')
    event.venueCoordinates = 'Point(' + str(adresstocoordinates(request.form.get('venueAddress'))[1]) + ' ' + str(adresstocoordinates(request.form.get('venueAddress'))[0]) + ')'
    event.startdate = correctdateTime(request.form.get('startTime'), request.form.get('date'))

def create_empytevent():
    newEvent = Event(
        FID=None, title=None, description=None, startdate=None, enddate=None, isRepetition=None,
        venueName=None, venueAddress=None,
        venueId=None, venueCoordinates=None, organizer=None, organizerName=None, organizerWebsite=None,
        ageRestriction=None,
        regularPrize=None, reducedPrize=None, category_id=None, category_name=None, picture=None, ticketsURL=None,
        moreInfoURL=None,
        facebookEventUrl=None, videoUrl=None)
    return newEvent


def adresstocoordinates(adress):  # adress is string
    geolocator = Nominatim(user_agent="kan det staa hva som helst??")
    location = geolocator.geocode(adress)
    return (location.latitude, location.longitude)


def coordinatestoadress(lat, lon):
    stringformat = (str(lat) + ',' + str(lon))  # From number input to string
    geolocator = Nominatim(user_agent="specify_your_app_name_here")
    return geolocator.reverse(stringformat)
    # returns full adress, ex:1, Elgeseter gate, Gløshaugen, Midtbyen, Trondheim, Trøndelag, 7030, Norge
