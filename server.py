from logging import DEBUG
from flask import Flask
from flask import render_template, url_for
from flask import request

from flask.helpers import url_for

app = Flask(__name__)

posts = [
    {
        "author": 'Amit',
        "title": "Learning is never stopping Step",
        "description": "I am Jr. Software Engineer",
        "posted_at": "May 1 2021"
    }
]


@app.get("/")
def index():
    return f"<p>Hello, world!</p>"


@app.get('/home')
def home():
    # app.logger.info('%s failed to log in', request)
    return render_template('home.html', posts=posts, title="First Blog")


@app.get('/image-resize')
def resize():
    app.logger.info('%s failed to log in', request)
    return render_template('image_resizer.html')


if __name__ == '__main__':
    app.run(debug=True)
