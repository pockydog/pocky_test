from models.school_models import Class, Teacher, Course

from app import db


class ClassHandler:
    @classmethod
    def get_info(cls, teacher_id, page, per_page):
        conditions = list()
        info_list = list()
        if teacher_id:
            conditions.append(Class.teacher_id == teacher_id)
        info = db.session.query(Class).filter(*conditions).paginate(
            page=page,
            per_page=per_page,
            error_out=False
        )
        pager = {
            'page': info.page,
            'per_page': info.per_page,
            'total_page': info.pages,
        }
        for info in info.items:
            results = {
                'id': info.id,
                'teacher_id': info.teacher_id,
                'course_id': info.course_id,
            }
            info_list.append(results)
        return info_list, pager

    @classmethod
    def del_info(cls, class_id):
        if not class_id:
            raise ValueError('Class id not exist')
        class_id = db.session.query(Class).filter(Class.id == class_id).first()
        if not class_id:
            raise ValueError('Class id not found')
        db.session.delete(class_id)
        db.session.commit()
        return {'success': True}

    @classmethod
    def update_info(cls, teacher_id, course_id):
        if not course_id:
            raise ValueError('Course id not exist')
        course = db.session.query(Class).filter(Class.course_id == course_id).first()
        if not course:
            raise ValueError('Course id not found')
        course.teacher_id = teacher_id
        db.session.add(course)
        results = {
            'id': course.id,
            'teacher_id': course.teacher_id,
            'course_id': course.course_id,
        }
        db.session.commit()
        return results

    @classmethod
    def add_info(cls, teacher_id, course_id):
        if not isinstance(teacher_id, int) and not isinstance(course_id, int):
            raise ValueError('wrong format')
        teacher = db.session.query(Teacher).filter(Teacher.id == teacher_id).first()
        course = db.session.query(Course).filter(Course.id == course_id).first()
        if not teacher:
            raise ValueError('teacher not found')
        if not course:
            raise ValueError('course not found')
        class_ = Class(
            teacher_id=teacher_id,
            course_id=course_id,
        )
        if not class_:
            raise ValueError('info not found')
        db.session.add(class_)
        db.session.commit()
        results = {
            'id': class_.id,
            'teacher_id': class_.teacher_id,
            'course_id': class_.course_id,
            'create_datetime': class_.create_datetime.strftime("%Y-%m-%d %H:%M")
        }
        return results

