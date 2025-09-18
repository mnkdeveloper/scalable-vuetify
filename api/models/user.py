
# app/models/user.py
from extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def to_dict(self):
        return {'id': self.id, 'username': self.username, 'email': self.email}

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
