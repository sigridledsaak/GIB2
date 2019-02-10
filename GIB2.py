from flask import Flask, render_template, url_for

app = Flask(__name__)

events = [
    {
        'name': 'SLAM POESI',
        'place': 'Litteraturhuset',
        'description': 'sykt opplegg'
    },
    {
        'name': 'HalvingFest',
        'place': 'NardoKlubbhus',
        'description': 'Var gøy'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', events=events)

@app.route('/about')
def about():
    return render_template('about.html', title ='About')


if __name__ == '__main__':
    app.run()
