from models.school_models import Student
from app import db


class SchoolHandler:
    @classmethod
    def get_info(cls, name, page, per_page):
        user_list = list()
        if name:
            users = db.session.query(Student).filter(Student.name == name).paginate(
                per_page=int(page),
                page=int(per_page),
                error_out=False
            )
        else:
            users = db.session.query(Student).paginate(
                per_page=int(page),
                page=int(per_page),
                error_out=False
            )
        for user in users:
            results = {
                'id': user.id,
                'name': user.name,
                'gender': user.gender,
                'grade': user.grade,
                'phone_number': user.phone_number,
                'create_datetime': user.create_datetime.strftime("%Y-%m-%d %H:%M"),
                'update_datetime': user.update_datetime.strftime("%Y-%m-%d %H:%M"),
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
        if not student:
            raise ValueError('Wrong format')
        db.session.add(student)
        db.session.commit()
        return {'success': True}

    @classmethod
    def delete_info(cls, student_name):
        student = db.session.query(Student).filter(Student.name == student_name).first()
        if not student:
            raise ValueError('Student name not exist')
        db.session.delete(student)
        db.session.commit()
        return {'success': True}

    @classmethod
    def update_info(cls, student_name, phone_number):
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

