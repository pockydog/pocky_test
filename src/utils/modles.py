import sys
from datetime import datetime

sys.path.append('/app')

from app import db

# from test_ import KelakitchenParser
# info_list = KelakitchenParser().get_product_info()



class test(db.Model):
    __tablename__ = 'test'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    dog_name = db.Column(db.String(100))
    dog_age = db.Column(db.Integer)

class Test_info(db.Model):
    __tablename__ = 'test_info'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    price = db.Column(db.Integer)
    type = db.Column(db.String(100))
    img_url = db.Column(db.String(1000))
    description = db.Column(db.String(10000))

class student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    create_time = db.Column(db.DateTime, default=datetime.now, nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'), nullable=False, comment='老師id')


class teacher(db.Model):
    __tablename__ ='teacher'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    create_time = db.Column(db.DateTime, default=datetime.now, nullable=False)

# db.create_all()

into = student(name='vicky', age='25', teacher_id=1)
db.session.add(into)
db.session.commit()

# # db.create_all()

