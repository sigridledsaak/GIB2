from app import db
from app.models import Event

def delete_all():
    events = db.session.query(Event).all()
    for event in events:
        db.session.delete(event)
    db.session.commit()

def main():
    delete_all()


if __name__ == "__main__":
    #"calling the function"
    main()