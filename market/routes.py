from crypt import methods
from flask import Flask, render_template, redirect, url_for, flash, request, jsonify
from market import APP
from market import forms
from market.model import Item, Users
from market.forms import RegistrationForm, LoginForm
from market import db
from flask_login import login_user
from flask_restful import Resource

@APP.route('/')
@APP.route('/home')
def homepage():
    return render_template('index.html')


@APP.route('/market')
def marketpage():
    ITEMS = Item.query.all()
    return render_template('market.html', items=ITEMS)


# Placeholders
@APP.route('/login', methods=['GET', 'POST'])
def login():
    form1 = LoginForm()

    if form1.validate_on_submit():
        attempted_user = Users.query.filter_by(username=form1.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form1.password1.data):
            login_user(attempted_user)
            flash(f"Welcome to KietMart {attempted_user.username}", category='success')
            return redirect(url_for('marketpage'))
        else:
            flash(f"User Name and Password are not correct Please Try again", category='danger')

    return render_template('login.html', form1=form1)


@APP.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user_to_create = Users(username=form.username.data, emailID=form.emailID.data,
                               password=form.password1.data)

        db.session.add(user_to_create)
        db.session.commit()

        return redirect(url_for('login'))

    if form.errors != {}:  # This shows that If there is Errors in the form which is stored in the form of dictionary
        for error_all in form.errors.values():
            flash(f"The Error is {error_all}", category='danger')

    return render_template('register.html', forms=form)

# API section
class API_TEST(Resource):

    def get(self):
        return jsonify({'message': 'Hello World'})

    # Corresponds to POST request
    def post(self):
        data = request.get_json()  # status code
        return jsonify({'data': data}), 201


# another resource to calculate the square of a number
class Square(Resource):

    def get(self, num):
        return jsonify({'square': num ** 2})

class FindUser(Resource):

    def get(self, username_given):
        find_user = Users.query.filter_by(username= username_given).first()
        if find_user:
            return jsonify({'user': find_user.username+' is found in the Database'})
        else:
            return jsonify({'user': 'Not Found'})