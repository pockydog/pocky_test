from models.school_models import ScoreRecord
from app import db


class ScoreRecordHandler:
    @classmethod
    def get_info(cls):
        info = db.session.query(ScoreRecord.score, ScoreRecord.schedule_id, ScoreRecord.id).all()
        result_list = list()
        for score, schedule_id, id_ in info:
            result = {
                'score': score,
                'schedule_id': schedule_id,
                'id': id_,
            }
            result_list.append(result)
        return result_list

    @classmethod
    def get_one_info(cls, schedule_id):
        info = db.session.query(ScoreRecord).filter(ScoreRecord.schedule_id == schedule_id).first()
        result = {
            'score': info.score,
            'schedule_id': info.schedule_id,
        }
        return result

    @classmethod
    def add_info(cls, score, schedule_id):
        info = ScoreRecord(
            score=score,
            schedule_id=schedule_id,
            )
        db.session.add(info)
        db.session.commit()
        return {'success': True}

    @classmethod
    def del_info(cls, schedule_id):
        info = db.session.query(ScoreRecord).filter(ScoreRecord.schedule_id == schedule_id).first()
        db.session.delete(info)
        db.session.commit()
        return {'success': True}

    @classmethod
    def update_info(cls, schedule_id, score):
        info = db.session.query(ScoreRecord).filter(ScoreRecord.schedule_id == schedule_id).first()
        if score:
            ScoreRecord.score = score
        if schedule_id:
            ScoreRecord.schedule_id = schedule_id
        db.session.add(info)
        db.session.commit()
        result = {
            'score': info.score,
            'schedule_id': info.schedule_id,
        }
        return result



