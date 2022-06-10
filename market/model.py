from market import db, login_manager
from market import bcrypt
from flask_login import UserMixin


# User for Login_Required
@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

# Class For Database Model of Users
class Users(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=20), nullable=False, unique=True)
    emailID = db.Column(db.String(length=250), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=255), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    item = db.relationship('Item', backref='owned_user', lazy=True)  # This Defines the RelationShip with the Item
    # Model That which Item is Associated to The User

    # User to Prettify the budget and add a ',' like before - 1000 , After 1,000
    @property
    def prettier_budget(self):
        if len(str(self.budget)) >= 4:
            return f'{str(self.budget)[:-3]},{str(self.budget)[-3:]}$'
        else:
            return f"{self.budget}$"

    # Used to Hash the Password by Creating its Getter
    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

# Class for Item Model in Database
class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=20), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=2555), nullable=False, unique=True)
    owner = db.Column(db.Integer(), db.ForeignKey('users.id'))

    def __repr__(self) -> str:
        return f'Items {self.id} {self.name}'
