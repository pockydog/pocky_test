from models.school_models import *


class EmergencyHandler:
    @classmethod
    def get_all_info(cls):
        emergency_contact = db.session.query(EmergencyContact.name, EmergencyContact.student_id, EmergencyContact.relationship_to_client, EmergencyContact.phone_number).all()
        result_list = list()
        for name, student_id, relationship_to_client, phone_number in emergency_contact:
            result = {
                'name': name,
                'student_id': student_id,
                'relationship_to_client': relationship_to_client,
                'phone_number': phone_number,

            }
            result_list.append(result)
        return result_list

    @classmethod
    def get_emergency_info(cls, emergency_student_id):
        emergency_contact = db.session.query(EmergencyContact).filter(EmergencyContact.student_id == emergency_student_id).first()
        results = {
            'name': emergency_contact.name,
            'student_id': emergency_student_id,
            'relationship_to_client': emergency_contact.relationship_to_client,
            'phone_number': emergency_contact.phone_number,
        }
        return results

    def add_emergency_info(self, name, student_id, relationship_to_client, phone_number):
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
    def delete_emergency_info(cls, student_id):
        emergency = db.session.query(EmergencyContact).filter(EmergencyContact.student_id == student_id).first()
        db.session.delete(emergency)
        db.session.commit()
        return {'success': True}

    @classmethod
    def update_emergency_info(cls, name, phone_number, relationship):
        user = db.session.query(EmergencyContact).filter(EmergencyContact.name == name).first()
        if phone_number:
            user.phone_number = phone_number
        if relationship:
            user.relationship_to_client = relationship
        db.session.add(user)
        db.session.commit()
        results = {
            'id': user.id,
            'name': user.name,
            'student_id': user.student_id,
            'relationship_to_client': user.relationship_to_client,
            'phone_number': user.phone_number,

        }
        return results
