from GIB2 import db


class exempleEvent(db.Model):
    __tablename__ = 'exEvent'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    desc = db.Column(db.String())


    def __init__(self, name, desc, published):
        self.name = name
        self.desc = desc


    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'desc': self.desc
        }