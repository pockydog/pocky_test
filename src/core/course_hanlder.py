from models.school_models import Course
from app import db


class CourseHanlder:
    @classmethod
    def get_info(cls, is_active, page, per_page):
        result_list = list()
        info = db.session.query(Course)
        if is_active:
            info = info.filter(Course.is_active == is_active)\
                .paginate(
                page=int(page),
                per_page=int(per_page),
                error_out=False
            )
            info_ = info.items
        else:
            info_ = info.paginate(
                page=int(page),
                per_page=int(per_page),
                error_out=False
            )
        for info in info_:
            results = {
                'name': info.name,
                'classroom_id': info.classroom_id,
                'open_datetime': info.open_time.strftime("%Y-%m-%d %H:%M"),
                'is_active': info.is_active,
            }
            result_list.append(results)
        return result_list

    @classmethod
    def add_info(cls, name, classroom_id, is_active, open_time):
        if not classroom_id:
            raise ValueError('Classroom id not exist')
        info = Course(name=name,
                      classroom_id=classroom_id,
                      is_active=is_active,
                      open_time=open_time,
                      )
        db.session.add(info)
        db.session.commit()
        return {'success': True}

    @classmethod
    def del_info(cls, name):
        info = db.session.query(Course).filter(Course.name == name).first()
        if not info:
            raise ValueError('Name not exist')
        db.session.delete(info)
        db.session.commit()
        return {'success': True}

    @classmethod
    def update_info(cls, name, classroom_id, is_active, open_time):
        info = db.session.query(Course).filter(Course.name == name).first()
        if not info:
            raise ValueError('Name not exist')
        Course.classroom_id = classroom_id
        Course.is_active = is_active
        Course.open_time = open_time
        db.session.add(info)
        results = {
            'name': info.name,
            'gender': info.gender,
            'phone_number': info.phone_number,
        }
        db.session.commit()
        return results

