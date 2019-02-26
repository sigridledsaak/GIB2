from flask import Flask, render_template, url_for
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
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html', title ='About')

@app.route('/register')
def register():
    return render_template('register.html',title='Register Event')

if __name__ == '__main__':
    app.run(debug=True)
