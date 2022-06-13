from schema import Schema, Or, And
# from utils.schema import SchoolSchema


class Schema:
    INFO = Schema({
        'name': str,
        'gender': int,
        'grade': int,
        'phone_number': Or(str, int),
    })
    SCOREINFO = Schema({
        'score': int,
        'schedule_id': int,
        'id': int,
    })
    TEACHERINFO = Schema({
        'name': str,
        'gender': Or(str, int),
        'phone_number': int,
    })
    EMERGENCYINFO = Schema({
        'id': int,
        'name': str,
        'student_id': int,
        'relationship_to_client': str,
        'phone_number': Or(str, int),
    })
    COURSEINFO = Schema({
        'name': str,
        'gender': str,
        'phone_number': Or(str, int),
    })
