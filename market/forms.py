from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, DataRequired, Email, ValidationError
from market.model import Users


class RegistrationForm(FlaskForm):

    def validate_username(self, user_to_check):
        user = Users.query.filter_by(username=user_to_check.data).first()
        if user:
            raise ValidationError('User Name Already Exist Please Try with Different user name')

    def validate_emailID(self, email_to_check):
        email = Users.query.filter_by(emailID=email_to_check.data).first()
        if email:
            raise ValidationError('User Email Already Exists Please Try with Different Email')

    username = StringField(label="Username", validators=[Length(min=4,max=40), DataRequired()])
    emailID = StringField(label="Email", validators=[Email(), DataRequired()])
    password1 = PasswordField(label="Password", validators=[Length(min=6), DataRequired()])
    confirm_password1 = PasswordField(label="Confirm password", validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label="Create Account")


class LoginForm(FlaskForm):
    username = StringField(label="Username", validators=[DataRequired()])
    password1 = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="Login")
