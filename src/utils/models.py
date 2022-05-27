import sys
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

class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    create_time = db.Column(db.DateTime, default=datetime.now, nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'), nullable=False, comment='老師id')

class Teacher(db.Model):
    __tablename__ ='teacher'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    create_time = db.Column(db.DateTime, default=datetime.now, nullable=False)

