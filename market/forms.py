from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, DataRequired, Email


class RegistrationForm(FlaskForm):
    username = StringField(label="Username", validators=[Length(min=4,max=40), DataRequired()])
    emailID = StringField(label="Email", validators=[Email(), DataRequired()])
    password1 = PasswordField(label="Password", validators=[Length(min=6), DataRequired()])
    confirm_password1 = PasswordField(label="Confirm password", validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label="Create Account")
