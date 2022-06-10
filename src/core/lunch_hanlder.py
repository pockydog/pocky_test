from models.models import Lunch
from app import db
from random import choice


class Test:
    @classmethod
    def add_info(cls, lunch_name):
        test = Lunch(
            lunch_name=lunch_name,
        )
        db.session.add(test)
        db.session.commit()
        return {'success': True}

    @classmethod
    def get_info(cls):
        info = db.session.query(Lunch.lunch_name).all()
        change = choice(info)
        result = {
            'lunch_name': f'{change.lunch_name}',
        }
        return result

    @classmethod
    def del_info(cls, name):
        info = db.session.query(Lunch.lunch_name == name).all()
        db.session.delete(info)
        db.session.commit()
        return {'success': True}






