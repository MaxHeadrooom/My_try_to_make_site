from flask import Flask
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new_database.db'
database = SQLAlchemy(application)


class Accounts(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    Login = database.Column(database.String(100), unique=True, nullable=False)
    Password = database.Column(database.String(100), nullable=False)
    date = database.Column(database.Date)
    reg_date = database.Column(database.DateTime, nullable=False)
    city = database.Column(database.String(100))
    street = database.Column(database.String(100))
    house = database.Column(database.String(100))

    def __repr__(self):
        return f'{self.id}'

class Basket(database.Model):
    id_b = database.Column(database.Integer, primary_key=True)
    cost = database.Column(database.Float, nullable = False)
    description = database.Column(database.String(100), nullable = False)
    customer_id = database.Column(database.Integer)


class Orders(database.Model):
    id_o = database.Column(database.Integer, primary_key=True, unique = True)
    customer_id = database.Column(database.Integer)
    price = database.Column(database.Float, nullable = False)
    
class Product(database.Model):
    idp = database.Column(database.Integer, unique = True, primary_key=True)
    name = database.Column(database.String(100))
    cost = database.Column(database.Float)

database.create_all()