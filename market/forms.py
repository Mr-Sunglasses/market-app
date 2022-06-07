from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, DataRequired, Email, ValidationError
from market.model import Users


class RegistrationForm(FlaskForm):

    def validate_username(self, user_to_check):
        user = Users.filter_by(username=user_to_check).first()
        if user:
            raise ValidationError('User Name Already Exist Please Try with Different user name')

    def git

    username = StringField(label="Username", validators=[Length(min=4,max=40), DataRequired()])
    emailID = StringField(label="Email", validators=[Email(), DataRequired()])
    password1 = PasswordField(label="Password", validators=[Length(min=6), DataRequired()])
    confirm_password1 = PasswordField(label="Confirm password", validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label="Create Account")
