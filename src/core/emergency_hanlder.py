from models.school_models import EmergencyContact, Student
from app import db


class EmergencyHandler:
    @classmethod
    def get_info(cls, student_id, page, per_page):
        conditions = list()
        result_list = list()
        if student_id:
            conditions.append(EmergencyContact.student_id == student_id)
        info = db.session.query(EmergencyContact).filter(*conditions).paginate(
            page=page,
            per_page=per_page,
            error_out=False,
        )
        pagers = {
            'page': info.page,
            'per_page': info.per_page,
            'total_page': info.pages,
        }
        for info in info.items:
            result = {
                'name': info.name,
                'student_id': info.student_id,
                'relationship_to_client': info.relationship_to_client,
                'phone_number': info.phone_number,
            }
            result_list.append(result)
        return result_list, pagers

    @classmethod
    def add_info(cls, name, student_id, relationship_to_client, phone_number):
        if not isinstance(student_id, int):
            raise ValueError('Student id wrong format')
        student = db.session.query(Student).filter(Student.id == student_id).first()
        if not student:
            raise ValueError('Student id not exist')
        emergency = EmergencyContact(
            name=name,
            student_id=student_id,
            relationship_to_client=relationship_to_client,
            phone_number=phone_number,
        )
        db.session.add(emergency)
        db.session.commit()
        result = {
            'id': emergency.id,
            'student_id': emergency.student_id,
            'name': emergency.name,
            'relationship_to_client': emergency.relationship_to_client,
            'phone_number': emergency.phone_number,
        }
        return result

    @classmethod
    def delete_info(cls, student_id):
        if not student_id:
            raise ValueError('Student Id not exist')
        emergency = db.session.query(EmergencyContact).filter(EmergencyContact.student_id == student_id).first()
        if not emergency:
            raise ValueError('student id not found')
        db.session.delete(emergency)
        db.session.commit()
        return {'success': True}

    @classmethod
    def update_info(cls, name, phone_number, relationship):
        if not name:
            raise ValueError('Name is not exist')
        user = db.session.query(EmergencyContact).filter(EmergencyContact.name == name).first()
        if not user:
            raise ValueError('user not found')
        user.phone_number = phone_number
        user.relationship_to_client = relationship
        db.session.add(user)
        results = {
            'id': user.id,
            'name': user.name,
            'student_id': user.student_id,
            'relationship_to_client': user.relationship_to_client,
            'phone_number': user.phone_number,
        }
        db.session.commit()
        return results

