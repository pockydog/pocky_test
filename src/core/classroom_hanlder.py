from models.school_models import Classroom
from app import db


class ClassroomHanlder:
    @classmethod
    def get_info(cls):
        info = db.session.query(Classroom.name, Classroom.location).all()
        result_list = list()
        for name, location in info:
            result = {
                'name': name,
                'location': location,
            }
            result_list.append(result)
        return result_list

    @classmethod
    def get_one_info(cls, name):
        info = db.session.query(Classroom).filter(Classroom.name == name).first()
        result = {
            'name': info.name,
            'location': info.location,
        }
        return result

    @classmethod
    def create_info(cls, name, location):
        info = Classroom(
            name=name,
            location=location,
        )
        db.session.add(info)
        db.session.commit()
        return {'success': True}

    @classmethod
    def del_info(cls, name):
        info = db.session.query(Classroom).filter(Classroom.name == name).first()
        db.session.delete(info)
        db.session.commit()
        return {'success': True}

    @classmethod
    def update_info(cls, classroom_name, name ,location):
        info = db.session.query(Classroom).filter(Classroom.name == classroom_name).first()
        if location:
            info.location = location
        if name:
            info.name = name
        db.session.add(info)
        db.session.commit()
        results = {
            'name': info.name,
            'location': info.location,
        }
        return results











