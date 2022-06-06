from market import db


class Users(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=20), nullable=False, unique=True)
    emailID = db.Column(db.String(length=250), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=255), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    item = db.relationship('Item', backref='owned_user', lazy=True)  # This Defines the RelationShip with the Item
    # Model That which Item is Associated to The User


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=20), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=2555), nullable=False, unique=True)
    owner = db.Column(db.Integer(), db.ForeignKey('users.id'))

    def __repr__(self) -> str:
        return f'Items {self.id} {self.name}'

