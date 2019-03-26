from app import db

from geoalchemy2.types import Geography


class Event(db.Model):
    __tablename__ = 'Event'

    ID = db.Column(db.Integer, primary_key=True, index=True)
    FID = db.Column(db.Integer, index=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    startdate = db.Column(db.TIMESTAMP)
    enddate = db.Column(db.TIMESTAMP)
    isRepetition = db.Column(db.BOOLEAN)
    venueName = db.Column(db.String)
    venueCoordinates = db.Column(Geography(geometry_type='POINT'))
    venueAddress = db.Column(db.String)
    venueId = db.Column(db.Integer)
    organizer = db.Column(db.String)
    organizerWebsite = db.Column(db.String)
    ageRestriction = db.Column(db.Integer)
    regularPrice = db.Column(db.Float)
    reducedPrice = db.Column(db.Float)
    category_id = db.Column(db.Integer)
    category_name = db.Column(db.String)
    picture = db.Column(db.String)
    listPictureURL = db.Column(db.String)
    ticketsURL = db.Column(db.String)
    moreInfoURL = db.Column(db.String)
    facebookEventUrl = db.Column(db.String)
    videoUrl = db.Column(db.String)


    def __init__(self, FID, title, description, startdate, enddate,
                 isRepetition, venueName, venueCoordinates, venueAddress,
                 venueId, organizer,
                 organizerName, organizerWebsite, ageRestriction, regularPrize, reducedPrize, category_id,
                 category_name, picture, ticketsURL, moreInfoURL, facebookEventUrl, videoUrl):
        self.FID = FID
        self.title = title
        self.description = description
        self.startdate = startdate
        self.enddate = enddate
        self.isRepetition = isRepetition
        self.venueName = venueName,
        self.venueCoordinates = venueCoordinates
        self.venueAddress = venueAddress
        self.venueId = venueId
        self.organizer = organizer
        self.organizerName = organizerName
        self.organizerWebsite = organizerWebsite
        self.ageRestriction = ageRestriction
        self.regularPrice = regularPrize
        self.reducedPrice = reducedPrize
        self.category_id = category_id
        self.category_name = category_name
        self.picture = picture
        self.ticketsURL = ticketsURL
        self.moreInfoURL = moreInfoURL
        self.facebookEventUrl = facebookEventUrl
        self.videoUrl = videoUrl

    def __repr__(self):
        return '<ID {}>'.format(self.ID)

    def serialize(self):
        return {
            'ID': self.ID,
            'FID': self.FID,
            'title': self.title,
            'description': self.description,
            'startdate': self.startdate,
            'enddate': self.enddate,
            'isRepetition': self.isRepetition,
            'venueName': self.venueName,
            'venueCoordinates': self.venueCoordinates,
            'venueAddress': self.venueAddress,
            'venueId': self.venueId,
            'organizer': self.organizer,
            'organizerName': self.organizerName,
            'organizerWebsite': self.organizerWebsite,
            'ageRestriction': self.ageRestriction,
            'regularPrize': self.regularPrice,
            'reducedPrize': self.reducedPrice,
            'category_id': self.category_id,
            'category_name': self.category_name,
            'picture': self.picture,
            'ticketsURL': self.ticketsURL,
            'moreInfoURL': self.moreInfoURL,
            'facebookEventUrl': self.facebookEventUrl,
            'videoUrl': self.videoUrl
        }

    CATEGORY_CHOICES = [
        "Concert", "Conference", "Course", "Exhibition", "Family",
        "Festival", "Lecture", "Literature", "Movies", "Other", "Quiz",
        "Senior", "Social", "Sport", "Technology", "Theater"
    ]

