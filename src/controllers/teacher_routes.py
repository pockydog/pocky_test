from app import app
from core.teacher_hanlder import TeacherHanlder
from flask import jsonify
from utils.payload_utils import PayloadUtils
from flask import request
from utils.school_schema import Schema


@app.route('/teacher', methods=['GET'])
def get_teacher_info():
    """
    名稱查詢單筆資料
    """
    name = request.args.get('name')
    results = TeacherHanlder.get_info(name=name)
    return jsonify(results=results)


@app.route('/teacher', methods=['POST'])
@PayloadUtils.inspect_schema(Schema.TEACHERINFO)
def create_teacher_info(payload):
    """
    建立老師資料
    """
    results = TeacherHanlder.add_info(
        name=payload['name'],
        gender=payload['gender'],
        phone_number=payload['phone_number'],

    )
    return jsonify(results=results)


@app.route('/teacher/del', methods=['DELETE'])
def delete_teacher_info():
    """
    移除老師資料
    """
    name = request.args.get('name')
    results = TeacherHanlder.delete_info(name=name)
    return jsonify(results=results)


@app.route('/teacher/update', methods=['PUT'])
@PayloadUtils.inspect_schema()
def update_teacher_info(payload):
    """
    修改資料
    """
    name = request.args.get('name')
    gender = payload['gender']
    phone_number = payload['phone_number']
    results = TeacherHanlder.update_info(phone_number=phone_number,
                                         gender=gender,
                                         name=name)
    return jsonify(results=results)
