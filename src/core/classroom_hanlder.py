from models.school_models import Classroom, Course
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
        result = {
            'id': info.id,
            'name': info.name,
            'location': info.location,
        }
        return result

    @classmethod
    def del_info(cls, classroom_id):
        if not classroom_id:
            raise ValueError('Classroom id wrong format')
        courses = db.session.query(Course).filter(Course.classroom_id == classroom_id).all()
        for course in courses:
            db.session.delete(course)
        classroom = db.session.query(Classroom).filter(Classroom.id == classroom_id).first()
        if not classroom:
            raise ValueError('Classroom id not found')
        db.session.delete(classroom)
        db.session.commit()
        return {'success': True}

    @classmethod
    def update_info(cls, classroom_id, name, location):
        if not isinstance(classroom_id, int):
            raise ValueError('Classroom id wrong format')
        classroom_id = db.session.query(Classroom).filter(Classroom.id == classroom_id).first()
        if not classroom_id:
            raise ValueError('Classroom id not found')
        classroom_id.location = location
        classroom_id.name = name
        db.session.add(classroom_id)
        results = {
            'name': classroom_id.name,
            'location': classroom_id.location,
        }
        db.session.commit()
        return results

