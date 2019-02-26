from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_dotenv import DotEnv
import os
from geoalchemy2.types import Geography

app = Flask(__name__)
#app.config.from_object(Config[Config.init_app()])

POSTGRES = {
    'user': 'postgres',
    'pw': 'password',
    'db': 'postgres',
    'host': 'localhost',
    'port': '5432',
}


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/postgres'#'postgresql://%(user)s:\
#%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

#db.init_app(app)

app.config.from_pyfile('config.py')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import *

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
