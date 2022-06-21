from models.school_models import Teacher, Class
from app import db


class TeacherHanlder:
    @classmethod
    def get_info(cls, name, page, per_page):
        conditions = list()
        result_list = list()
        if name:
            conditions.append(Teacher.name == name)
        info_ = db.session.query(Teacher).filter(*conditions).paginate(
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
                'name': info.name,
                'gender': info.gender,
                'phone_number': info.phone_number,
            }
            result_list.append(result)
        return result_list, pagers

    @classmethod
    def add_info(cls, name, gender, phone_number):
        if not isinstance(name, str) and not isinstance(phone_number, str) and not isinstance(gender, int):
            raise ValueError('Wrong format')
        user = Teacher(
            name=name,
            gender=gender,
            phone_number=phone_number,
        )
        db.session.add(user)
        db.session.commit()
        return {'success': True}

    @classmethod
    def delete_info(cls, teacher_id):
        if not teacher_id:
            raise ValueError('Teacher id not exist')
        classes_ = db.session.query(Class).filter(Class.teacher_id == teacher_id).all()
        if not classes_:
            raise ValueError('Class id not found')
        for class_ in classes_:
            db.session.delete(class_)
        teacher = db.session.query(Teacher).filter(Teacher.id == teacher_id).first()
        if not teacher:
            raise ValueError('User not found')
        db.session.delete(teacher)
        db.session.commit()
        return {'success': True}

    @classmethod
    def update_info(cls, name, phone_number, gender):
        if not name:
            raise ValueError('Teacher name not exist')
        user = db.session.query(Teacher).filter(Teacher.name == name).first()
        if not user:
            raise ValueError('user not found')
        user.phone_number = phone_number
        user.gender = gender
        db.session.add(user)
        result = {
            'id': user.id,
            'name': user.name,
            'gender': user.gender,
            'phone_number': user.phone_number,
        }
        db.session.commit()
        return result

