from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

APP = Flask(__name__)
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'

db = SQLAlchemy(APP)

## This is because routes are dependent on APP variable
from market import routes
