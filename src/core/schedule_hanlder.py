from models.school_models import Schedule
from app import db


class ScheduleHanlder:
    @classmethod
    def get_info(cls, class_id):
        result_list = list()
        if class_id:
            schedule_ = db.session.query(Schedule).filter(Schedule.class_id == class_id).all()
        else:
            schedule_ = db.session.query(Schedule).all()
        for schedule in schedule_:
            result = {
                'id': schedule.id,
                'student_id': schedule.student_id,
                'class_id': schedule.class_id,
            }
            result_list.append(result)
        return result_list

    @classmethod
    def add_info(cls, student_id, class_id):
        if not student_id:
            raise ValueError('Student id not found')
        if not class_id:
            raise ValueError('Class id not found')
        schedule = Schedule(
            student_id=student_id,
            class_id=class_id,
        )
        db.session.add(schedule)
        db.session.commit()
        return {'success': True}

    @classmethod
    def del_info(cls, class_id):
        schedule = db.session.query(Schedule).filter(Schedule.class_id == class_id).first()
        if not schedule:
            raise ValueError('Class id not found')
        db.session.delete(schedule)
        db.session.commit()
        return {'success': True}

    @classmethod
    def update_info(cls, student_id, class_id):
        schedule = db.session.query(Schedule).filter(Schedule.student_id == student_id).first()
        if not schedule:
            raise ValueError('Student id not found')
        Schedule.class_id = class_id
        db.session.add(schedule)
        results = {
            'id': schedule.id,
            'class_id': schedule.class_id,
            'student_id': schedule.student_id,
        }
        db.session.commit()
        return results

