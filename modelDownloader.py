import os
import re
import xml.etree.ElementTree as ET

import requests

from app import db
from app.models import Event


# loading n amount of pages
def loadRSS(n, m):
    # looping trough the selected amount of pages, writing down objects

    for x in range(n, m):
        # url of rss feed
        url = 'https://trdevents.no/en/feed/?paged=' + str(x)

        # creating HTTP response object from given url
        resp = requests.get(url)

        # saving the xml file
        with open('topeventfeed/' + str(x) + '.xml', 'wb') as f:
            a = (str(resp.content.decode("utf-8")))

            regex = re.compile(r"&(?!amp;|lt;|gt;)")
            a = regex.sub("&amp;", a)

            f.write(bytes(a, 'utf-8'))
            print("skrevet til fil")


def parseXML(xmlfile):
    # create element tree object

    tree = ET.parse(xmlfile, ET.XMLParser(encoding="utf-8"))

    # get root element
    root = tree.getroot()

    # create empty list for news items
    eventsitems = []

    # iterate news items
    for item in root.findall('./channel/item'):

        event = Event(
            FID=None, title=None, description=None, startdate=None, enddate=None, isRepetition=None,
            venueName=None, venueAddress=None,
            venueId=None, venueCoordinates=None, organizer=None, organizerName=None, organizerWebsite=None,
            ageRestriction=None,
            regularPrize=None, reducedPrize=None, category_id=None, category_name=None, picture=None, ticketsURL=None,
            moreInfoURL=None,
            facebookEventUrl=None, videoUrl=None
        )

        eventfields = []

        if item:
            for subitem in item:
                if subitem.text:
                    eventfields.append([subitem.tag, subitem.text])
                    for subsubitem in subitem:
                        if subsubitem.text:
                            if '{Event}' in subsubitem.tag:
                                eventfields.append(
                                    [subsubitem.tag.split('{Event}', 1)[1], subsubitem.text.replace('\n', '').strip()])
                            for subsubsubitem in subsubitem:
                                if subsubsubitem:
                                    for subsubsubsubitem in subsubsubitem:
                                        if subsubsubsubitem.text:
                                            eventfields.append((subsubsubsubitem.tag, subsubsubsubitem.text))

        lat = 0
        lng = 0

        for f in eventfields:
            if f[0] == 'title':
                event.title = f[1]
            if f[0] == 'id':
                event.FID = f[1]
            if f[0] == 'description':
                event.description = f[1]
            if f[0] == 'isRecurrent':
                if f[1] == 'no':
                    event.isRepetition = False
                if f[1] == 'yes':
                    event.isRepetition = True
            if f[0] == 'startdate':
                event.startdate = f[1]
            if f[0] == 'enddate':
                event.enddate = f[1]
            if f[0] == 'categoryID':
                event.category_id = f[1]
            if f[0] == 'categoryName':
                event.category_name = f[1]
            if f[0] == 'venueId':
                event.venueId = f[1]
            if f[0] == 'venueName':
                event.venueName = f[1]
            if f[0] == 'venueStreet':
                event.venueAddress = f[1]
            if f[0] == 'venueLat':
                if f[1] == '':
                    lat = None
                else:
                    lat = float(f[1])
            if f[0] == 'venueLng':
                if f[1] == '':
                    lng = None
                else:
                    lng = float(f[1])
            if f[0] == 'organizer':
                event.organizer = f[1]
            if f[0] == 'organizerFacebook':
                event.organizerWebsite = f[1]
            if f[0] == 'picture':
                event.picture = f[1]
            if f[0] == 'normalPrice':
                event.regularPrice = f[1]
            if f[0] == 'reducedPrize':
                event.reducedPrice = f[1]
            if f[0] == 'ageRestriction':
                if f[1] == '':
                    event.ageRestriction = None
                else:
                    event.ageRestriction = f[1]
            if f[0] == 'videoUrl':
                event.videoUrl = f[1]
            if f[0] == 'moreInfoUrl':
                event.moreInfoURL = [1]
            if f[0] == 'facebookEventUrl':
                event.facebookEventUrl = f[1]
        if lat is not None and lng is not None:
            event.venueCoordinates = 'Point(' + str(lng) + ' ' + str(lat) + ')'
        eventsitems.append(event)

    return eventsitems


# get the last element in the database that has a FID
def get_last_object_with_fid():
    return db.session.query(Event).order_by(Event.FID.desc()).first()


def main(n, m):
    # load rss from web to update existing xml file
    loadRSS(n, m)

    Eventitems = []

    checkobject = get_last_object_with_fid()
    directory = os.fsencode('topeventfeed')

    # parse xml files
    for filename in os.listdir(directory):

        if filename.endswith(bytes('.xml', 'utf-8')):

            Eventitems = parseXML(os.path.join(directory, filename))

            Eventitems.sort(key=lambda x: x.FID, reverse=True)
            for event in Eventitems:
                if checkobject is None:
                    print('Adding object:', event.FID)
                    db.session.add(event)
                    db.session.commit()

                else:
                    print(checkobject.FID)
                    if int(checkobject.FID) != int(event.FID):
                        print('Adding object:', event.FID)
                        db.session.add(event)
                        db.session.commit()

                    else:
                        print('Object already exist!', event.FID)
                        for filename in os.listdir(directory):
                            if filename.endswith(bytes('.xml', 'utf-8')):
                                os.remove(os.path.join(directory, filename))
                        return

            os.remove(os.path.join(directory, filename))

        else:
            continue


if __name__ == "__main__":
    # calling main function
    main(1, 10)
