from sqlalchemy import func

from app import db


class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(90), nullable=True)
    gender = db.Column(db.Boolean(), comment='0:男, 1:女')
    grade = db.Column(db.Integer, server_default='4', comment='年級 1:高一 2:高二 3:高三 4:尚未選擇')
    phone_number = db.Column(db.String(30), nullable=False)
    create_datetime = db.Column(db.DateTime, server_default=func.now())
    update_datetime = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    emergency_contact = db.relationship('EmergencyContact', cascade='all, delete-orphan')
    schedule = db.relationship('Schedule', uselist=False)


class EmergencyContact(db.Model):
    __tablename__ = 'emergency_contact'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    name = db.Column(db.String(90), nullable=True)
    relationship_to_client = db.Column(db.String(90), nullable=True)
    phone_number = db.Column(db.String(30), nullable=True)
    create_datetime = db.Column(db.DateTime, server_default=func.now())
    update_datetime = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())


class Classroom(db.Model):
    __tablename__ = 'classroom'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(90), nullable=True)
    location = db.Column(db.String(500))
    create_datetime = db.Column(db.DateTime, server_default=func.now())
    update_datetime = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    course = db.relationship('Course', backref='classroom')


class Teacher(db.Model):
    __tablename__ = 'teacher'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(90), nullable=True)
    gender = db.Column(db.Boolean())
    phone_number = db.Column(db.String(30))
    create_datetime = db.Column(db.DateTime, server_default=func.now())
    update_datetime = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    classes = db.relationship('Class', backref='class_teacher')


class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(90), nullable=True)
    classroom_id = db.Column(db.Integer, db.ForeignKey('classroom.id'))
    is_active = db.Column(db.Integer, server_default='2', comment='年級 1:是 2:否')
    open_time = db.Column(db.DateTime, server_default=None)
    create_datetime = db.Column(db.DateTime, server_default=func.now())
    update_datetime = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    class_course = db.relationship('Class', backref='classcourse')


class Class(db.Model):
    __tablename__ = 'class'
    id = db.Column(db.Integer, primary_key=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    create_datetime = db.Column(db.DateTime, server_default=func.now())
    update_datetime = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    class_schedule = db.relationship('Schedule', uselist=False)


class Schedule(db.Model):
    __teblename__ = 'schedule'
    id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey('class.id'))
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    create_datetime = db.Column(db.DateTime, server_default=func.now())
    update_datetime = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    scoree = db.relationship('ScoreRecord', backref='scorelist')


class ScoreRecord(db.Model):
    __tablename__ = 'score_record'
    id = db.Column(db.Integer, primary_key=True)
    schedule_id = db.Column(db.Integer, db.ForeignKey('schedule.id'))
    score = db.Column(db.Integer)
    create_datetime = db.Column(db.DateTime, server_default=func.now())
    update_datetime = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())


