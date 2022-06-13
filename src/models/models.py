from app import db


class Lunch(db.Model):
    __tablename__ = 'lunch'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    lunch_name = db.Column(db.String(90), nullable=True, unique=True)


