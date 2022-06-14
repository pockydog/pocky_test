from models.school_models import Student
from app import db


class SchoolHandler:
    @classmethod
    def get_info(cls, name):
        user_list = list()
        if name:
            users = db.session.query(Student).filter(Student.name == name).all()
        else:
            users = db.session.query(Student).all()
        for user in users:
            results = {
                'id': user.id,
                'name': user.name,
                'gender': user.gender,
                'grade': user.grade,
                'phone_number': user.phone_number,
                'create_datetime': user.create_datetime.strftime("%Y-%m-%d %H:%M:%S"),
                'update_datetime': user.update_datetime.strftime("%Y-%m-%d %H:%M:%S"),
            }
            user_list.append(results)
        return user_list


    @classmethod
    def add_info(cls, name, gender, grade, phone_number):
        student = Student(
            name=name,
            gender=gender,
            grade=grade,
            phone_number=phone_number,
        )
        db.session.add(student)
        db.session.commit()
        return {'success': True}

    @classmethod
    def delete_info(cls, student_name):
        student = db.session.query(Student).filter(Student.name == student_name).first()
        db.session.delete(student)
        db.session.commit()
        return {'success': True}

    @classmethod
    def update_info(cls, student_name, phone_number):
        user = db.session.query(Student).filter(Student.name == student_name).first()
        if phone_number:
            user.phone_number = phone_number
        db.session.add(user)
        db.session.commit()
        results = {
            'id': user.id,
            'name': user.name,
            'gender': user.gender,
            'grade': user.grade,
            'phone_number': user.phone_number,
            'create_datetime': user.create_datetime.strftime("%Y-%m-%d %H:%M:%S"),
            'update_datetime': user.update_datetime.strftime("%Y-%m-%d %H:%M:%S"),
        }
        return results

