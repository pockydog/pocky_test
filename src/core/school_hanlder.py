from models.school_models import *


class SchoolHandler:
    @classmethod
    def get_info(cls):
        student_list = db.session.query(Student.id, Student.name, Student.gender, Student.grade, Student.phone_number, Student.create_datetime, Student.update_datetime).all()
        result_list = list()
        for id, name, gender, grade, phone_number, create_datetime, update_datetime in student_list:
            result = {
                'id': id,
                'name': name,
                'gender': gender,
                'grade': grade,
                'phone_number': phone_number,
                'create_datetime': create_datetime,
                'update_datetime': update_datetime,
            }
            result_list.append(result)
        return result_list

    @classmethod
    def get_student(cls, name):
        user = db.session.query(Student).filter(Student.name == name).first()
        results = {
            'id': user.id,
            'name': name,
            'gender': user.gender,
            'grade': user.grade,
            'phone_number': user.phone_number,
            'create_datetime': user.create_datetime,
            'update_datetime': user.update_datetime,
        }
        return results

    def get_my_info(self, student_id):
        user = db.session.query(Student).filter(Student.id == student_id).first()
        results = {
            'id': user.id,
            'name': user.name,
            'gender': user.gender,
            'grade': user.grade,
            'phone_number': user.phone_number,
            'create_datetime': user.create_datetime,
            'update_datetime': user.update_datetime,
        }
        return results

    def add_info(self, name, gender, grade, phone_number):
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

