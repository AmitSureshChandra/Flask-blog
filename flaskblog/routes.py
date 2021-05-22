from flask import render_template, url_for, redirect, flash, request
from flaskblog.form import RegistrationForm, LoginForm
from flaskblog.bootstrap import app, db, bcrypt
from flaskblog.models import User, Post
from flask_login import login_user, current_user
posts = []


@app.get('/home')
@app.get('/')
def home():
    # app.logger.info('%s failed to log in', request)
    return render_template('home.html', posts=posts, title="First Blog")


@app.get('/about')
def about():
    # app.logger.info('%s failed to log in', request)
    return render_template('about.html', posts=posts, title="About")


@app.route('/register', methods=["GET", "POST"])
def register():
    
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(username=form.username.data,
                    email=form.email.data, password=hashed_password)

        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created! You are able to login',
              category='success')
        return redirect(url_for('login'))
    else:
        app.logger.info('%s failed to register', request)
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        flash(f'Login unsuccessful . Please check email & password',
              category='danger')
    return render_template('login.html', title='Login', form=form)
