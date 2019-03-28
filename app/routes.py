import datetime as dt
from flask import render_template, request
from sqlalchemy import or_, and_
from app import app, db
from .models import Event
from shapely import wkb
import geoalchemy2.functions as ga
from geoalchemy2.elements import WKTElement
from geopy.geocoders import Nominatim


@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():

    def convertCoordinates(hexlocation):
        point = wkb.loads(hexlocation, hex=True)
        long = point.x
        lat = point.y
        return [lat, long]

    datetime = dt.datetime.now()
    delta = datetime + dt.timedelta(days=4)

    defaultEvents = db.session.query(Event.title, Event.ageRestriction, Event.category_name, Event.startdate, Event.venueCoordinates,Event.facebookEventUrl,Event.venueName,Event.venueAddress)\
                .filter(Event.startdate >= datetime, Event.startdate <= delta)

    defaultCords = []

    for event in defaultEvents:
        if event.venueCoordinates is not None:
            coord = convertCoordinates(str(event.venueCoordinates))
            defaultCords.append(coord)
        else:
            if event.venueAddress is not None:
                try :
                    c = adresstocoordinates((event.venueAddress))
                    defaultCords.append(c)
                except:
                    defaultCords.append('None')
            else :
                defaultCords.append('None')

    if request.method == 'POST':
        #Get user input from form
        date = request.form.get('date')
        time = request.form.get('time')
        category = request.form.get('category')
        ticketPrize = request.form.get('ticketPrize')
        ageLimit = request.form.get('ageLimit')
        pos = request.form.get('pos')
        distance = request.form.get('distance')

        lat_user, long_user = float(pos.split(',')[0]), float(pos.split(',')[1])
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
        if pos and distance:
            user_point = WKTElement('POINT({} {})'.format(pos.split(',')[1],pos.split(',')[0]))
            filters.append(ga.ST_Distance(Event.venueCoordinates, user_point) <= distance)

        events = db.session.query(Event.title, Event.ageRestriction, Event.category_name, Event.startdate,
                                  Event.venueCoordinates,Event.facebookEventUrl,Event.venueName,
                                  Event.venueAddress).filter(and_(*filters)).all()


        cords = []
        for event in events:
            if event.venueCoordinates is not None:
                coord = convertCoordinates(str(event.venueCoordinates))
                cords.append(coord)
            else:
                if event.venueAddress is not None:
                    c = adresstocoordinates((event.venueAddress))
                    cords.append(c)
                else :
                    cords.append('None')

        return render_template('home.html', categories=Event.CATEGORY_CHOICES, events=events, latlong=cords,lat_user = lat_user, long_user = long_user, distance = distance)
    return render_template('home.html', categories=Event.CATEGORY_CHOICES, events=defaultEvents, latlong=defaultCords)



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
    if (location is None):
        return 'None'
    else :
        return [location.latitude, location.longitude]


def coordinatestoadress(lat, lon):
    stringformat = (str(lat) + ',' + str(lon))  # From number input to string
    geolocator = Nominatim(user_agent="specify_your_app_name_here")
    return geolocator.reverse(stringformat)
    # returns full adress, ex:1, Elgeseter gate, Gløshaugen, Midtbyen, Trondheim, Trøndelag, 7030, Norge