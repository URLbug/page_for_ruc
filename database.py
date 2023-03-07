import os

from flask_sqlalchemy import SQLAlchemy

from __init__ import app


basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    def __init__(self, first_name, last_name, email, about):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.about = about
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    about = db.Column(db.String(1000), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f'<User {self.username}>'