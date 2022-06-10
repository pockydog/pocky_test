from models.school_models import Class
from app import db


class ClassHandler:
    @classmethod
    def get_info(cls):
        info = db.session.query(Class.id, Class.teacher_id, Class.course_id).all()
        info_list = list()
        for id_, teacher_id, course_id in info:
            results = {
                'id': id_,
                'teacher_id': teacher_id,
                'course_id': course_id,
            }
            info_list.append(results)
        return info_list

    @classmethod
    def get_one_info(cls, teacher_id):
        info = db.session.query(Class).filter(Class.teacher_id.ilike('title%') == teacher_id).all()
        info_list = list()
        for id_ in info:
            results = {
                'teacher_id': id_.teacher_id,
                'course_id': id_.course_id,
            }
            info_list.append(results)

        return info_list

    @classmethod
    def add_info(cls, teacher_id, course_id):
        class_ = Class(
            teacher_id=teacher_id,
            course_id=course_id
        )
        db.session.add(class_)
        db.session.commit()
        return {'success': True}

    @classmethod
    def del_info(cls,  teacher_id):
        info = db.session.query(Class).filter(Class.teacher_id == teacher_id).first()
        db.session.delete(info)
        db.session.commit()
        return {'success': True}

    @classmethod
    def update_info(cls, teacher_id, course_id):
        user = db.session.query(Class).filter(Class.course_id == course_id).first()
        if teacher_id:
            user.teacher_id = teacher_id
        db.session.add(user)
        db.session.commit()
        results = {
            'id': user.id,
            'teacher_id': user.teacher_id,
            'course_id': user.course_id,
        }
        return results

    @classmethod
    def get_emergency_info(cls, name):
        emergency = db.session.query(Class).filter(Class.name == name).first()
        results = {
            'emergency_contact': emergency,
        }
        return results

