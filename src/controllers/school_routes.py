from app import app
from core.school_hanlder import SchoolHandler
from flask import jsonify
from utils.payload_utils import PayloadUtils
from flask import request
from utils.school_schema import *


@app.route('/get-info', methods=['GET'])
def get_info():
    """
    取得所有學生資料
    """
    results = SchoolHandler.get_info()
    return jsonify(results=results)


@app.route('/student', methods=['GET'])
def get_student():
    """
    名稱查詢單筆資料
    """
    name = request.args.get('name')
    if name is None or name not in SchoolHandler.get_info():
        results = SchoolHandler.get_info()
    else:
        results = SchoolHandler.get_student(name=name)
    return jsonify(results=results)


@app.route('/student/new', methods=['POST'])
@PayloadUtils.inspect_schema(Schemalist.INFO)
def create_info(payload):
    """
    建立學生資料
    """
    results = SchoolHandler().add_info(
        name=payload['name'],
        gender=payload['gender'],
        grade=payload['grade'],
        phone_number=payload['phone_number'],
    )
    return jsonify(results=results)


@app.route('/delete-info', methods=['DELETE'])
def delete_info():
    """
    移除學生資料
    """
    name = request.args.get('name')
    results = SchoolHandler().delete_info(student_name=name)
    return jsonify(results=results)


@app.route('/student/update', methods=['PUT'])
@PayloadUtils.inspect_schema()
def update_info(payload):
    """
    修改學生資料
    """
    try:
        results = SchoolHandler.update_info(student_name=request.args.get('name'),
                                            phone_number=payload['phone_number'])
    except:
        return 'no data exists'
    return jsonify(results=results)
