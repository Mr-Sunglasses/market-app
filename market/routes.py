from flask import Flask, render_template
from market import APP
from market.model import Item


@APP.route('/')
@APP.route('/home')
def homepage():
    return render_template('index.html')


@APP.route('/market')
def marketpage():
    ITEMS = Item.query.all()
    print(ITEMS)
    return render_template('market.html', items=ITEMS)


# Placeholders
@APP.route('/login')
def login():
    return f"<h1>Login</h1>"


@APP.route('/register')
def register():
    return "<h1>Register</h1>"