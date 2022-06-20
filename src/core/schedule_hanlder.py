from models.school_models import Schedule, Student, Class
from app import db


class ScheduleHanlder:
    @classmethod
    def get_info(cls, class_id, page, per_page):
        result_list = list()
        conditions = list()
        if class_id:
            conditions.append(Schedule.class_id == class_id)
        info_ = db.session.query(Schedule).filter(*conditions).paginate(
            page=page,
            per_page=per_page,
            error_out=False
        )
        pagers = {
            'page': info_.page,
            'per_page': info_.per_page,
            'total_page': info_.pages,
        }
        for info in info_.items:
            result = {
                'id': info.id,
                'student_id': info.student_id,
                'class_id': info.class_id,
            }
            result_list.append(result)
        return result_list, pagers

    @classmethod
    def add_info(cls, student_id, class_id):
        if not isinstance(student_id, int) and isinstance(class_id, int):
            raise ValueError('Wrong format')
        student = db.session.query(Student).filter(Student.id == student_id).first()
        if not student:
            raise ValueError('Student id not found')
        class_ = db.session.query(Class).filter(Class.id == class_id).first()
        if not class_:
            raise ValueError('Class id not found')
        schedule = Schedule(
            student_id=student_id,
            class_id=class_id,
        )
        db.session.add(schedule)
        db.session.commit()
        result = {
            'id': schedule.id,
            'class_id': schedule.class_is,
            'student_id': schedule.student_id,
        }
        return result

    @classmethod
    def del_info(cls, class_id):
        if not class_id:
            raise ValueError('Class id not exist')
        schedule = db.session.query(Schedule).filter(Schedule.class_id == class_id).first()
        if not schedule:
            raise ValueError('class id not found')
        db.session.delete(schedule)
        db.session.commit()
        return {'success': True}

    @classmethod
    def update_info(cls, student_id, class_id):
        if not student_id:
            raise ValueError('Student id not exist')
        schedule = db.session.query(Schedule).filter(Schedule.student_id == student_id).first()
        if not schedule:
            raise ValueError('student id not found')
        Schedule.class_id = class_id
        db.session.add(schedule)
        results = {
            'id': schedule.id,
            'class_id': schedule.class_id,
            'student_id': schedule.student_id,
        }
        db.session.commit()
        return results

