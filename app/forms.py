from flask_wtf  import FlaskForm
from wtforms import StringField, IntegerField, DateField
from wtforms.validators import *

class EventForm(FlaskForm):
    ID = IntegerField('ID' )#Why comma here?
    title = StringField('tittel', validators=[DataRequired()])
    description = StringField('description')
    startDate = DateField('startDate')
    venueName = StringField('venueName')
    address = StringField('address')
    category = StringField('category')
    agelimit = IntegerField('ageLimit')
    ticketPrice = IntegerField('ticketPrice')
    oragnizerWebsite = StringField('organizerWebsite')



    # Does form need all event attributes?


