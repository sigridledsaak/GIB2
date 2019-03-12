from app import db
from geoalchemy2.types import Geography


class Event(db.Model):
    __tablename__ = 'Event'

    ID = db.Column(db.Integer, primary_key=True)
    titel = db.Column(db.String)
    beskrivelse = db.Column(db.String)
    startDate = db.Column(db.DATE)
    startTime = db.Column(db.TIME)
    endDate = db.Column(db.DATE)
    isRepetition = db.Column(db.BOOLEAN)
    venueName = db.Column(db.String)
    venueCoordinates = db.Column(Geography(geometry_type='POINT'))
    venueAddress = db.Column(db.String)
    venueID = db.Column(db.Integer)
    organizerID = db.Column(db.Integer)
    organizerName = db.Column(db.String)
    organizerWebsite = db.Column(db.String)
    ageLimit = db.Column(db.Integer)
    regularTicketPrice = db.Column(db.Float)
    reducedTicketPrice = db.Column(db.Float)
    category_id = db.Column(db.Integer)
    category_name = db.Column(db.String)
    pictureURL = db.Column(db.String)
    listPictureURL = db.Column(db.String)
    ticketsURL = db.Column(db.String)
    moreInfoURL = db.Column(db.String)
    facebookURL = db.Column(db.String)
    videosURL = db.Column(db.String)


    def __init__(self, titel, beskrivelse, startDate, startTime, endDate,
                 isRepetition, venueName, venueCoordinates, venueAddress,
                 venueID, organizerID, organizerName, organizerWebsite,
                 ageLimit, regularTicketPrize, reducedTicketPrize, category_id,
                 category_name, pictureURL, ticketsURL, moreInfoURL, facebookURL, videosURL):

        self.titel = titel
        self.beskrivelse = beskrivelse
        self.startDate = startDate
        self.startTime = startTime
        self.endDate = endDate
        self.isRepetition = isRepetition
        self.venueName = venueName,
        self.venueCoordinates = venueCoordinates
        self.venueAddress = venueAddress
        self.venueID = venueID
        self.organizerID = organizerID
        self.organizerName = organizerName
        self.organizerWebsite = organizerWebsite
        self.ageLimit = ageLimit
        self.regularTicketPrice = regularTicketPrize
        self.reducedTicketPrice = reducedTicketPrize
        self.category_id = category_id
        self.category_name = category_name
        self.pictureURL = pictureURL
        self.ticketsURL = ticketsURL
        self.moreInfoURL = moreInfoURL
        self.facebookURL = facebookURL
        self.videosURL = videosURL


    def __repr__(self):
        return '<ID {}>'.format(self.ID)

    def serialize(self):
        return {
            'ID': self.ID,
            'titel': self.titel,
            'beskrivelse': self.beskrivelse,
            'startDate': self.startDate,
            'startTime': self.startTime,
            'endDate': self.endDate,
            'isRepetition': self.isRepetition,
            'venueName': self.venueName,
            'venueCoordinates': self.venueCoordinates,
            'venueAddress': self.venueAddress,
            'venueID': self.venueID,
            'organizerID': self.organizerID,
            'organizerName': self.organizerName,
            'organizerWebsite': self.organizerWebsite,
            'ageLimit': self.ageLimit,
            'regularTicketPrize': self.regularTicketPrice,
            'reducedTicketPrize': self.reducedTicketPrice,
            'category_id': self.category_id,
            'category_name': self.category_name,
            'pictureURL': self.pictureURL,
            'ticketsURL': self.ticketsURL,
            'moreInfoURL': self.moreInfoURL,
            'facebookURL': self.facebookURL,
            'videosURL': self.videosURL
        }