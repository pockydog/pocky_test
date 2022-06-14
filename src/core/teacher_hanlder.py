from models.school_models import Teacher
from app import db


class TeacherHanlder:
    @classmethod
    def get_info(cls, name):
        result_list = list()
        if name:
            user_ = db.session.query(Teacher).filter(Teacher.name == name).first()
        else:
            user_ = db.session.query(Teacher.name, Teacher.gender, Teacher.phone_number).all()
        for user in user_:
            result = {
                'name': user.name,
                'gender': user.gender,
                'phone_number': user.phone_number,
            }
            result_list.append(result)
        return result_list



    @classmethod
    def add_info(cls, name, gender, phone_number):
        user = Teacher(
            name=name,
            gender=gender,
            phone_number=phone_number,
        )
        db.session.add(user)
        db.session.commit()
        return {'success': True}

    @classmethod
    def delete_info(cls, name):
        user = db.session.query(Teacher).filter(Teacher.name == name).first()
        db.session.delete(user)
        db.session.commit()
        return {'success': True}

    @classmethod
    def update_info(cls, name, phone_number, gender):
        user = db.session.query(Teacher).filter(Teacher.name == name).first()
        if phone_number:
            user.phone_number = phone_number
        if gender:
            user.gender = gender
        db.session.add(user)
        db.session.commit()
        results = {
            'name': user.name,
            'gender': user.gender,
            'phone_number': user.phone_number,
        }
        return results






