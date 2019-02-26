import GIB2
from flask import render_template

@GIB2.route('/')
@GIB2.route('/index')
def index():
    return "Hello, World!"