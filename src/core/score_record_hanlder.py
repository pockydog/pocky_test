from models.school_models import ScoreRecord, Schedule
from app import db


class ScoreRecordHandler:
    @classmethod
    def get_info(cls, schedule_id, page, per_page):
        result_list = list()
        conditions = list()
        if schedule_id:
            conditions.append(ScoreRecord.schedule_id == schedule_id)
        info_ = db.session.query(ScoreRecord).filter(*conditions).paginate(
            page=page,
            per_page=per_page,
            error_out=False
        )
        pagers = {
            'page': info_.page,
            'per_page': info_.per_page,
            'total_page': info_.pages,
        }
        for info in info_:
            result = {
                'score': info.score,
                'schedule_id': info.schedule_id,
                'id': info.id,
            }
            result_list.append(result)
        return result_list, pagers

    @classmethod
    def add_info(cls, score, schedule_id):
        if not isinstance(schedule_id, int):
            raise ValueError('Schedule Id wrong format')
        schedule = db.session.query(Schedule).filter(Schedule.id == schedule_id).first()
        if not schedule:
            raise ValueError('Schedule Id not exist')
        info = ScoreRecord(
            score=score,
            schedule_id=schedule_id,
            )
        db.session.add(info)
        result = {
            'score': info.score,
            'schedule_id': info.schedule_id,
        }
        db.session.commit()
        return result

    @classmethod
    def del_info(cls, id_):
        condition = list()
        if id_:
            condition.append(
                ScoreRecord.id == id_
            )
        info = db.session.query(ScoreRecord).filter(
            *condition
        ).all()
        if not info:
            raise ValueError('Id not found')
        db.session.delete(info)
        db.session.commit()
        return {'success': True}

    @classmethod
    def update_info(cls, schedule_id, score):
        if not schedule_id:
            raise ValueError('schedule id not found')
        info = db.session.query(ScoreRecord).filter(ScoreRecord.schedule_id == schedule_id).first()
        if not info:
            raise ValueError('schedule id not found')
        ScoreRecord.score = score
        ScoreRecord.schedule_id = schedule_id
        db.session.add(info)
        result = {
            'score': info.score,
            'schedule_id': info.schedule_id,
        }
        db.session.commit()

        return result

