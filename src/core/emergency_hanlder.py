from models.school_models import EmergencyContact
from app import db


class EmergencyHandler:
    @classmethod
    def get_info(cls, student_id, page, per_page):
        result_list = list()
        if student_id:
            emergency_contact = db.session.query(EmergencyContact).filter(EmergencyContact.student_id == student_id).first()
        else:
            emergency_contact = db.session.query(EmergencyContact).paginate(
                page=int(page),
                per_page=int(per_page),
                error_out=False
            )
        for emergency in emergency_contact:
            result = {
                'name': emergency.name,
                'student_id': emergency.student_id,
                'relationship_to_client': emergency.relationship_to_client,
                'phone_number': emergency.phone_number,
            }
            result_list.append(result)
        return result_list

    @classmethod
    def add_info(cls, name, student_id, relationship_to_client, phone_number):
        if not student_id:
            raise ValueError('Student id not exist')
        emergency = EmergencyContact(
            name=name,
            student_id=student_id,
            relationship_to_client=relationship_to_client,
            phone_number=phone_number,
        )
        db.session.add(emergency)
        db.session.commit()
        return {'success': True}

    @classmethod
    def delete_info(cls, student_id):
        emergency = db.session.query(EmergencyContact).filter(EmergencyContact.student_id == student_id).first()
        if not student_id:
            raise ValueError('Student id not exist')
        db.session.delete(emergency)
        db.session.commit()
        return {'success': True}

    @classmethod
    def update_info(cls, name, phone_number, relationship):
        user = db.session.query(EmergencyContact).filter(EmergencyContact.name == name).first()
        if not name:
            raise ValueError('Name not exist')
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
