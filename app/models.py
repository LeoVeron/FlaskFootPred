from flask_login import UserMixin
from . import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) 
    password = db.Column(db.String(100))
    pseudo = db.Column(db.String(1000))
    
class Upcoming_matches(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(150))
    url = db.Column(db.String(150))
    
    
