from flask_wtf import FlaskForm
from wtforms import StringField,EmailValidator,DataRequired


class RegisterationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min = 2,max= 20)])
    email = StringField('Email', validators=[DataRequired(), EmailValidator()])
    password = PasswordField('Email', validators=[DataRequired(), EmailValidator()])
