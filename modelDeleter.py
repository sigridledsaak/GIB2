import os
import datetime as dt

from app import db
from app.models import Event

def delete_old_events():
    datetime = dt.datetime.now()
    delta = datetime + dt.timedelta(days=-1)
    events = db.session.query(Event).filter(Event.startdate <= delta).all()
    for event in events:
        print(event)
        db.session.delete(event)
    db.session.commit()

    return "Outdated events deleted!"

def main():
    delete_old_events()


if __name__ == "__main__":
    #"calling the function"
    main()
