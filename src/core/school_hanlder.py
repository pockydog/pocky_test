from models.school_models import Student, EmergencyContact
from app import db


class SchoolHandler:
    @classmethod
    def get_info(cls, name, page, per_page):
        conditions = list()
        user_list = list()
        if name:
            conditions.append(Student.name == name)
        info_ = db.session.query(Student).filter(*conditions).paginate(
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
            results = {
                'id': info.id,
                'name': info.name,
                'gender': info.gender,
                'grade': info.grade,
                'phone_number': info.phone_number,
                'create_datetime': info.create_datetime.strftime("%Y-%m-%d %H:%M"),
                'update_datetime': info.update_datetime.strftime("%Y-%m-%d %H:%M"),
            }
            user_list.append(results)
        return user_list, pagers

    @classmethod
    def add_info(cls, name, gender, grade, phone_number):
        if not isinstance(name, str) and isinstance(gender, int) and isinstance(grade, int) and isinstance(phone_number, int):
            raise ValueError('Wrong format')
        user = Student(
            name=name,
            gender=gender,
            grade=grade,
            phone_number=phone_number,
        )
        db.session.add(user)
        db.session.commit()
        result = {
            'id': user.id,
            'name': user.name,
            'gender': user.gender,
            'grade': user.grade,
            'phone_number': user.phone_number,
            'create_datetime': user.create_datetime.strftime("%Y-%m-%d %H:%M:%S"),
            'update_datetime': user.update_datetime.strftime("%Y-%m-%d %H:%M:%S"),
        }
        return result

    @classmethod
    def delete_info(cls, student_id):
        emergencys = db.session.query(EmergencyContact).filter(EmergencyContact.student_id == student_id).all()
        if not emergencys:
            raise ValueError('student_id not found')
        for emergency in emergencys:
            db.session.delete(emergency)
        student = db.session.query(Student).filter(Student.id == student_id).first()
        if not student:
            raise ValueError('Student not found')
        db.session.delete(student)
        db.session.commit()
        return {'result': 'ok'}

    @classmethod
    def update_info(cls, student_name, phone_number):
        if not student_name:
            raise ValueError('Student name not exist')
        user = db.session.query(Student).filter(Student.name == student_name).first()
        if not user:
            raise ValueError('Student name not exist')
        user.phone_number = phone_number
        db.session.add(user)
        results = {
            'id': user.id,
            'name': user.name,
            'gender': user.gender,
            'grade': user.grade,
            'phone_number': user.phone_number,
            'create_datetime': user.create_datetime.strftime("%Y-%m-%d %H:%M:%S"),
            'update_datetime': user.update_datetime.strftime("%Y-%m-%d %H:%M:%S"),
        }
        db.session.commit()
        return results

