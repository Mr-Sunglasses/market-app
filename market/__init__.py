from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from market.SEACRETKEY import KEY

APP = Flask(__name__)
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
APP.config['SECRET_KEY'] = KEY

db = SQLAlchemy(APP)

## This is because routes are dependent on APP variable
from market import routes
