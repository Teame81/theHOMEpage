import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from myAPIkeys import TheKeys, appSecretKey
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SECRET_KEY'] = appSecretKey

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app,db)

class TimmieHome(db.Model):
    __tablename__ = 'timmiehome'
    id = db.Column(db.Integer, primary_key=True)
    home_or_not = db.Column(db.Boolean)

    def __init__(self, home_or_not):
        self.home_or_not = home_or_not

    def __repr__(self):
        if self.home_or_not == True:
            return f"Timmie is home!"
        elif self.home_or_not == False:
            return f"Timmie is away!"
        else:
            return f"No input yet"
