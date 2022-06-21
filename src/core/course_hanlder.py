from datetime import datetime

from models.school_models import Course, Classroom
from app import db


class CourseHanlder:
    @classmethod
    def get_info(cls, is_active, page, per_page):
        conditions = list()
        result_list = list()
        if is_active:
            conditions.append(Course.is_active == is_active)
        info_ = db.session.query(Course).filter(*conditions).paginate(
            page=page,
            per_page=per_page,
            error_out=False
        )
        pager = {
            'page': info_.page,
            'per_page': info_.per_page,
            'total_page': info_.pages,
        }
        for info in info_.items:
            results = {
                'name': info.name,
                'classroom_id': info.classroom_id,
                'open_datetime': info.open_time.strftime("%Y-%m-%d %H:%M"),
                'is_active': info.is_active,
            }
            result_list.append(results)
        return result_list, pager

    @classmethod
    def add_info(cls, name, classroom_id, is_active, open_time):
        if not isinstance(classroom_id, int):
            raise ValueError('Classroom Id wrong format')
        classroom = db.session.query(Classroom).filter(Classroom.id == classroom_id).first()
        if not classroom:
            raise ValueError('Classroom Id not exist')
        info = Course(name=name,
                      classroom_id=classroom_id,
                      is_active=is_active,
                      open_time=open_time,
                      )
        db.session.add(info)
        db.session.commit()
        result = {
            'id': info.id,
            'name': info.name,
            'classroom_id': info.classroom_id,
            'is_active': info.is_active,
            'open_time': datetime.date(info.open_time).strftime("%A") + info.open_time.strftime(" %H:%M"),

        }
        return result

    @classmethod
    def del_info(cls, classroom_id):
        if not classroom_id:
            raise ValueError('Classroom id wrong format')
        courses = db.session.query(Course).filter(Course.classroom_id == classroom_id).all()
        if not courses:
            raise ValueError('Classroom id not found')
        for course in courses:
            db.session.delete(course)
        classroom = db.session.query(Classroom).filter(Classroom.id == classroom_id).first()
        db.session.delete(classroom)
        db.session.commit()
        return {'success': True}

    @classmethod
    def update_info(cls, name, classroom_id, is_active, open_time):
        if not name:
            raise ValueError('Name not exist')
        user = db.session.query(Course).filter(Course.name == name).first()
        if not user:
            raise ValueError('user not found')
        Course.classroom_id = classroom_id
        Course.is_active = is_active
        Course.open_time = open_time
        db.session.add(user)
        results = {
            'name': user.name,
            'gender': user.gender,
            'phone_number': user.phone_number,
        }
        db.session.commit()
        return results

