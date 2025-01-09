from __init__ import db

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username= db.Column(db.String)
    password= db.Column(db.String)

    def __str__(self):
        return f"ID: {self.id} Name: {self.username}"