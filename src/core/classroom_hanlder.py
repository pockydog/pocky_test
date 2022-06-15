from models.school_models import Classroom
from app import db


class ClassroomHanlder:
    @classmethod
    def get_info(cls, name, page, per_page):
        result_list = list()
        if name:
            info_ = db.session.query(Classroom).filter(Classroom.name == name).paginate(
                per_page=int(page),
                page=int(per_page),
                error_out=False
            )
        else:
            info_ = db.session.query(Classroom).paginate(
                per_page=int(page),
                page=int(per_page),
                error_out=False
            )
        for info in info_:
            result = {
                'name': info.name,
                'location': info.location,
            }
            result_list.append(result)
        return result_list

    @classmethod
    def add_info(cls, name, location):
        info = Classroom(
            name=name,
            location=location,
        )
        if not info:
            raise ValueError('Wrong format')
        db.session.add(info)
        db.session.commit()
        return {'success': True}

    @classmethod
    def del_info(cls, name):
        info = db.session.query(Classroom).filter(Classroom.name == name).first()
        if not info:
            raise ValueError('Name not exist')
        db.session.delete(info)
        db.session.commit()
        return {'success': True}

    @classmethod
    def update_info(cls, classroom_name, name, location):
        info = db.session.query(Classroom).filter(Classroom.name == classroom_name).first()
        if not info:
            raise ValueError('Name not exist')
        info.location = location
        info.name = name
        db.session.add(info)
        results = {
            'name': info.name,
            'location': info.location,
        }
        db.session.commit()
        return results

