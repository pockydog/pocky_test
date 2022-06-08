from app import app
from core.teacher_hanlder import *
from flask import jsonify
from utils.payload_utils import PayloadUtils
from flask import request


@app.route('/teacher', methods=['GET'])
def get_info():
    """
    名稱查詢單筆資料
    """
    name = request.args.get('name')
    if name is None or name not in TeacherHanlder.get_info():
        results = TeacherHanlder.get_info()
    else:
        results = TeacherHanlder.get_id_info(name=name)
    return jsonify(results=results)


@app.route('/teacher/new', methods=['POST'])
@PayloadUtils.inspect_schema()
def create_info(payload):
    """
    建立老師資料
    """
    results = TeacherHanlder.add_info(
        name=payload['name'],
        gender=payload['gender'],
        phone_number=payload['phone_number'],

    )
    return jsonify(results=results)


@app.route('/teacher/delete', methods=['DELETE'])
def delete_info():
    """
    移除老師資料
    """
    name = request.args.get('name')
    results = TeacherHanlder().delete_info(name=name)
    return jsonify(results=results)


@app.route('/teacher/update', methods=['PUT'])
@PayloadUtils.inspect_schema()
def update_info(payload):
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
