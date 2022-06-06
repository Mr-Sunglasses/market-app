import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('KEY_TO_ACCESS')

APP = Flask(__name__)
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
APP.config['SECRET_KEY'] = SECRET_KEY

db = SQLAlchemy(APP)

## This is because routes are dependent on APP variable
from market import routes
