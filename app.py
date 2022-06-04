from flask import Flask, render_template
from data.model import ITEMS

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def homepage():
    return render_template('index.html')


@app.route('/market')
def marketpage():

    return render_template('market.html',items = ITEMS)
























# Placehoders
@app.route('/login')
def login():
    return f"<h1>Login</h1>"

@app.route('/register')
def register():
    return "<h1>Register</h1>"



if __name__ == "__main__":

    app.run(debug=True,port=5500)