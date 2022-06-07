from crypt import methods
from flask import Flask, render_template, redirect, url_for
from market import APP
from market import forms
from market.model import Item, Users
from market.forms import RegistrationForm
from market import db


@APP.route('/')
@APP.route('/home')
def homepage():
    return render_template('index.html')


@APP.route('/market')
def marketpage():
    ITEMS = Item.query.all()
    return render_template('market.html', items=ITEMS)


# Placeholders
@APP.route('/login')
def login():
    return f"<h1>Login</h1>"


@APP.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user_to_create = Users(username=form.username.data, emailID=form.emailID.data,
                               password_hash=form.password1.data)

        db.session.add(user_to_create)
        db.session.commit()

        return redirect(url_for('marketpage'))

    if form.errors != {}:  # This shows that If there is Errors in the form which is stored in the form of dictionary
        for error_all in form.errors.values():
            print(f"The Error is {error_all}")

    return render_template('register.html', forms=form)
