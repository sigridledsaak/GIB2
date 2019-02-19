from flask import Flask, render_template, url_for

app = Flask(__name__)

events = [
    {
        'ID': '1',
        'Title': 'Slam Poesi',
        'Description': 'Total Hodemist',
        'startDate': '29.03.19',
        'startTime': '18:00',
        'endDate': '29.03.19',
        'venueName': 'Litteraturhuset',
        'venueCoordinates': '63.4, 10.4'
    },
    {
        'ID': '2',
        'Title': 'Halvingfest',
        'Description': 'Total Hodemist',
        'startDate': '02.02.19',
        'startTime': '18:00',
        'endDate': '02.02.19',
        'venueName': 'Litteraturhuset',
        'venueCoordinates': '63.4, 10.4'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', events=events)

@app.route('/about')
def about():
    return render_template('about.html', title ='About')

@app.route('/register')
def register():
    return render_template('register.html',title='Register Event')

if __name__ == '__main__':
    app.run(debug=True)
