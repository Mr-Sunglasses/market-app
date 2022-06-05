from flask import Flask, render_template
from data.model import ITEMS

APP = Flask(__name__)

@APP.route('/')
@APP.route('/home')
def homepage():
    return render_template('index.html')


@APP.route('/market')
def marketpage():

    return render_template('market.html',items = ITEMS)
























# Placehoders
@APP.route('/login')
def login():
    return f"<h1>Login</h1>"

@APP.route('/register')
def register():
    return "<h1>Register</h1>"



if __name__ == "__main__":

    APP.run(debug=True,port=5500)