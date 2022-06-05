from enum import unique
from app import APP
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(APP)

class Item(db.Model):

    name = db.Column(db.String(length=255), nullable= False , unique=True)