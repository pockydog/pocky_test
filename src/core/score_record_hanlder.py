from models.school_models import ScoreRecord
from app import db


class ScoreRecordHandler:
    @classmethod
    def get_info(cls, schedule_id, page, per_page):
        result_list = list()
        if schedule_id:
            info_ = db.session.query(ScoreRecord).filter(ScoreRecord.schedule_id == schedule_id).paginate(
                page=int(page),
                per_page=int(per_page),
                error_out=False
            )
        else:
            info_ = db.session.query(ScoreRecord).paginate(
                page=int(page),
                per_page=int(per_page),
                error_out=False
            )
        for info in info_:
            result = {
                'score': info.score,
                'schedule_id': info.schedule_id,
                'id': info.id,
            }
            result_list.append(result)
        return result_list

    @classmethod
    def add_info(cls, score, schedule_id):
        if not schedule_id:
            raise ValueError('Schedule id not exist')
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
        if not info:
            raise ValueError('Schedule id not exist')
        db.session.delete(info)
        db.session.commit()
        return {'success': True}

    @classmethod
    def update_info(cls, schedule_id, score):
        info = db.session.query(ScoreRecord).filter(ScoreRecord.schedule_id == schedule_id).first()
        if not info:
            raise ValueError('Schedule id not exist')
        ScoreRecord.score = score
        ScoreRecord.schedule_id = schedule_id
        db.session.add(info)
        result = {
            'score': info.score,
            'schedule_id': info.schedule_id,
        }
        db.session.commit()

        return result



