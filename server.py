from logging import DEBUG
from types import MethodType
from flask import Flask, render_template, url_for, redirect, request
from flask.helpers import flash
from datetime import datetime

from form import RegistrationForm, LoginForm

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '64c7f09d88e0edd7a4230c2181f40811'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(
        db.String(120), nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)

    posts = db.relationship('Post', backref="author", lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}','{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


posts = [
    {
        "author": 'Amit',
        "title": "Learning is never stopping Step",
        "description": "I am Jr. Software Engineer",
        "posted_at": "May 1 2021"
    }


]


@ app.get('/home')
@ app.get('/')
def home():
    # app.logger.info('%s failed to log in', request)
    return render_template('home.html', posts=posts, title="First Blog")


@ app.get('/about')
def about():
    # app.logger.info('%s failed to log in', request)
    return render_template('about.html', posts=posts, title="About")


@ app.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'user created for {form.username.data}', category='success')
        return redirect(url_for('home'))
    else:
        app.logger.info('%s failed to register', request)
    return render_template('register.html', title='Register', form=form)


@ app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'You have been logged in', category='success')
            return redirect(url_for('home'))
        else:
            flash(f'Login unsuccessful . Please check username & password',
                  category='danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
