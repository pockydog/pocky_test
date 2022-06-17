from models.school_models import Classroom
from app import db


class ClassroomHanlder:
    @classmethod
    def get_info(cls, name, page, per_page):
        conditions = list()
        result_list = list()
        if name:
            conditions.append(Classroom.name == name)
        info = db.session.query(Classroom).filter(*conditions).paginate(
            page=page,
            per_page=per_page,
            error_out=False
        )
        pagers = {
            'page': info.page,
            'per_page': info.per_page,
            'total_page': info.pages,
        }
        for info in info.items:
            result = {
                'name': info.name,
                'location': info.location,
            }
            result_list.append(result)
        return result_list, pagers

    @classmethod
    def add_info(cls, name, location):
        if not isinstance(name, str) and not isinstance(location, str):
            raise ValueError('Wrong format')
        info = Classroom(
            name=name,
            location=location,
        )
        db.session.add(info)
        db.session.commit()
        return {'success': True}

    @classmethod
    def del_info(cls, id_):
        if not id_:
            raise ValueError('data not found')
        info = db.session.query(Classroom).filter(Classroom.id == id_).first()
        if not id_:
            raise ValueError('Classroom id not exist')
        db.session.delete(info)
        db.session.commit()
        return {'success': True}

    @classmethod
    def update_info(cls, classroom_id, name, location):
        if not classroom_id:
            raise ValueError('data not found')
        info = db.session.query(Classroom).filter(Classroom.id == classroom_id).first()
        if not id_:
            raise ValueError('Classroom id not exist')
        info.location = location
        info.name = name
        db.session.add(info)
        results = {
            'name': info.name,
            'location': info.location,
        }
        db.session.commit()
        return results

