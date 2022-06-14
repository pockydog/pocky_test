from models.school_models import Schedule
from app import db


class ScheduleHanlder:
    @classmethod
    def get_info(cls, class_id):
        if class_id:
            schedule_ = db.session.query(Schedule).filter(Schedule.class_id == class_id).all()
        else:
            schedule_ = db.session.query(Schedule.id, Schedule.student_id, Schedule.class_id).all()
        result_list = list()
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
        db.session.delete(schedule)
        db.session.commit()
        return {'success': True}

    @classmethod
    def update_info(cls, student_id, class_id):
        schedule = db.session.query(Schedule).filter(Schedule.student_id == student_id).first()
        if class_id:
            Schedule.class_id = class_id
        db.session.add(schedule)
        db.session.commit()
        results = {
            'id': schedule.id,
            'class_id': schedule.class_id,
            'student_id': schedule.student_id,
        }
        return results

