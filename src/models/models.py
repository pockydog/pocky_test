from datetime import datetime
from app import db


class Test(db.Model):
    __tablename__ = 'test'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    dog_name = db.Column(db.String(100))
    dog_age = db.Column(db.Integer)


class TestInfo(db.Model):
    __tablename__ = 'test_info'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    price = db.Column(db.Integer)
    type = db.Column(db.String(100))
    img_url = db.Column(db.String(1000))
    description = db.Column(db.String(10000))

