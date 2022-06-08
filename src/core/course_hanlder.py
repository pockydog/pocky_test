from models.school_models import Course
from app import db


class CourseHanlder:
    @classmethod
    def get_info(cls):
        info = db.session.query(Course.name, Course.classroom_id, Course.is_active, Course.open_time).all()
        info_list = list()
        for name, classroom_id, is_active, open_time in info:
            results = {
                'name': name,
                'classroom_id': classroom_id,
                'is_active': is_active,
                'open_time': open_time,
            }
            info_list.append(results)
        return info_list

    @classmethod
    def add_info(cls, name, classroom_id, is_active, open_time):
        info = Course(name=name,
                      classroom_id=classroom_id,
                      is_active=is_active,
                      open_time=open_time,
                      )
        db.session.add(info)
        db.session.commit()
        return {'success': True}

    @classmethod
    def del_info(cls, name):
        info = db.session.query(Course).filter(Course.name == name).first()
        db.session.delete(info)
        db.session.commit()
        return {'success': True}

    @classmethod
    def update_info(cls, name, classroom_id, is_active, open_time):
        info = db.session.query(Course).filter(Course.name == name).first()
        if classroom_id:
            Course.classroom_id = classroom_id
        if is_active:
            Course.is_active = is_active
        if open_time:
            Course.open_time = open_time
        db.session.add(info)
        db.session.commit()
        results = {
            'name': info.name,
            'gender': info.gender,
            'phone_number': info.phone_number,
        }
        return results


