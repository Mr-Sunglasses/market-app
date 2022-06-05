from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy



APP = Flask(__name__)

db = SQLAlchemy(APP)
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
class Item(db.Model):

    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(length=20), nullable= False , unique=True)
    price = db.Column(db.Integer(), nullable = False)
    barcode = db.Column(db.String(length=12), nullable = False,unique = True)
    description = db.Column(db.String(length=2555), nullable = False , unique = True)

    def __repr__(self) -> str:
        return f'Items {self.id} {self.name}'





@APP.route('/')
@APP.route('/home')
def homepage():
    return render_template('index.html')


@APP.route('/market')
def marketpage():
    ITEMS = Item.query.all()
    print(ITEMS)
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