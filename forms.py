from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, EqualTo
import email_validator

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email()])

    password = PasswordField('Password', validators=[InputRequired()])

    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo(password)])

    submit = SubmitField('Login')