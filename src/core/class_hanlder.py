from models.school_models import Class
from app import db


class ClassHandler:
    @classmethod
    def get_info(cls, teacher_id, page ,per_page):
        info_list = list()
        if teacher_id:
            info_ = db.session.query(Class).filter(Class.teacher_id == teacher_id).paginate(
                per_page=int(page),
                page=int(per_page),
                error_out=False
            )
        else:
            info_ = db.session.query(Class).paginate(
                per_page=int(page),
                page=int(per_page),
                error_out=False
            )
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
        if not teacher_id:
            raise ValueError('Teacher id not exist')
        if not course_id:
            raise ValueError('Course id not exist')
        class_ = Class(
            teacher_id=teacher_id,
            course_id=course_id
        )
        db.session.add(class_)
        db.session.commit()
        return {'success': True}

    @classmethod
    def del_info(cls, class_id):
        info = db.session.query(Class).filter(Class.id == class_id).first()
        if not info:
            raise ValueError('Class id not exist')
        db.session.delete(info)
        db.session.commit()
        return {'success': True}

    @classmethod
    def update_info(cls, teacher_id, course_id):
        user = db.session.query(Class).filter(Class.course_id == course_id).first()
        if not user:
            raise ValueError('Course id not found')
        user.teacher_id = teacher_id
        db.session.add(user)
        results = {
            'id': user.id,
            'teacher_id': user.teacher_id,
            'course_id': user.course_id,
        }
        db.session.commit()
        return results

