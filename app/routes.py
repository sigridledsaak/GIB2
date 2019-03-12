from flask import render_template
from app import app
from app.models import Event, db
from geoalchemy2 import Geography
import psycopg2
from ppygis3 import Point


@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/')
@app.route('/home')
def home():
    lng = 10
    lat = 20
    venueCoordinates = 'Point(' + str(lng) + ' ' + str(lat) + ')'
    testEvent = Event(titel='firstEvent', startTime='00:00:00.0000000', beskrivelse='dette er det første eventet',startDate='0001-01-01' ,ageLimit=20, endDate='0001-01-01',
                      isRepetition=False, venueName='Samf', venueCoordinates = venueCoordinates, venueAddress='gate', venueID=0,
                      organizerID=0, organizerName=0, organizerWebsite='hei.no', regularTicketPrize=200,
                      reducedTicketPrize=100, category_id=0, category_name='fest', pictureURL=0, ticketsURL=0,
                      moreInfoURL=0, facebookURL=0, videosURL=0)

    testEvent2 = Event(titel='secondEvent', startTime='00:00:00.0000000', beskrivelse='dette er det første eventet',
                      startDate='0001-01-01', ageLimit=20, endDate='0001-01-01',
                      isRepetition=False, venueName='Samf', venueCoordinates=venueCoordinates, venueAddress='gate',
                      venueID=0,
                      organizerID=0, organizerName=0, organizerWebsite='hei.no', regularTicketPrize=200,
                      reducedTicketPrize=100, category_id=0, category_name='fest', pictureURL=0, ticketsURL=0,
                      moreInfoURL=0, facebookURL=0, videosURL=0)

    db.session().add(testEvent)
    db.session().add(testEvent2)
    db.session().commit()
    events = Event.query.all()
    print(events)

    for event in events:
        print (event.venueCoordinates)







    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html', title ='About')

@app.route('/register')
def register():
    return render_template('register.html',title='Register Event')


