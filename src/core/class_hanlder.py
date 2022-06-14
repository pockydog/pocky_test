from models.school_models import Class
from app import db


class ClassHandler:
    @classmethod
    def get_info(cls, teacher_id):
        info_list = list()
        if teacher_id:
            info_ = db.session.query(Class).filter(Class.teacher_id == teacher_id).all()
        else:
            info_ = db.session.query(Class.id, Class.teacher_id, Class.course_id).all()
        for info in info_:
            results = {
                'id': info.id,
                'teacher_id': info.teacher_id,
                'course_id': info.course_id,
            }
            info_list.append(results)
        return info_list

    @classmethod
    def add_info(cls, teacher_id, course_id):
        try:
            class_ = Class(
                teacher_id=teacher_id,
                course_id=course_id
            )
            db.session.add(class_)
            db.session.commit()
        except Exception:
            return ''
        return {'success': True}

    @classmethod
    def del_info(cls, id_):
        try:
            info = db.session.query(Class).filter(Class.id == id_).first()
            db.session.delete(info)
            db.session.commit()
        except Exception:
            return ''
        return {'success': True}

    @classmethod
    def update_info(cls, teacher_id, course_id):
        user = db.session.query(Class).filter(Class.course_id == course_id).first()
        try:
            user.teacher_id = teacher_id
            db.session.add(user)
            db.session.commit()
            results = {
                'id': user.id,
                'teacher_id': user.teacher_id,
                'course_id': user.course_id,
            }
        except Exception:
            return ''
        return results
