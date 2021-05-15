from flask import Flask, render_template, url_for, redirect, flash, request
from flaskblog.form import RegistrationForm, LoginForm
from flaskblog.bootsrap import app

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
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'user created for {form.username.data}', category='success')
        return redirect(url_for('home'))
    else:
        app.logger.info('%s failed to register', request)
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=["GET", "POST"])
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
