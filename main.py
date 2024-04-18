
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about-us')
def about_us():
    return render_template('about-us.html')

@app.route('/blind-runners-israel')
def blind_runners_israel():
    return render_template('blind-runners-israel.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/contact-us')
def contact_us():
    return render_template('contact-us.html')

if __name__ == '__main__':
    app.run(debug=True)
