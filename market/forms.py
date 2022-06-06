from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


class RegistrationForm(FlaskForm):
    username = StringField(label="Username")
    emailID = StringField(label="Email")
    password1 = PasswordField(label="Password")
    confirm_password1 = PasswordField(label="Confirm password")
    submit = SubmitField(label="Create Account")
