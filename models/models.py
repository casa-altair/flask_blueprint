""" models.py: Define the database here """
from app import db

class User(db.Model):
    """ Defining User DB Class """
    __tablename__ = "My Users"
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(80), nullable=False)
    user_email = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self, user_name, user_email):
        self.user_name = user_name
        self.user_email = user_email
