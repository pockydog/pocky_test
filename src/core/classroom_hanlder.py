from models.school_models import Classroom
from app import db


class ClassroomHanlder:
    @classmethod
    def get_info(cls, name):
        result_list = list()
        if name:
            info_ = db.session.query(Classroom).filter(Classroom.name == name).all()
        else:
            info_ = Classroom.query.all()
        for info in info_:
            result = {
                'name': info.name,
                'location': info.location,
            }
            result_list.append(result)
        return result_list

    # @classmethod
    # def create_info(cls, name, location):
    #     info = Classroom(
    #         name=name,
    #         location=location,
    #     )
    #     db.session.add(info)
    #     db.session.commit()
    #     return {'success': True}

    @classmethod
    def del_info(cls, name):
        info = db.session.query(Classroom).filter(Classroom.name == name).first()
        db.session.delete(info)
        db.session.commit()
        return {'success': True}


    @classmethod
    def update_info(cls, classroom_name, name, location):
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

