from app import app
from core.school_hanlder import SchoolHandler
from flask import jsonify
from utils.payload_utils import PayloadUtils
from flask import request
from utils.school_schema import Schema


@app.route('/student', methods=['GET'])
def get_student_info():
    """
    名稱查詢單筆資料
    """
    name = request.args.get('name')
    results = SchoolHandler.get_info(name=name)
    return jsonify(results=results)


@app.route('/student', methods=['POST'])
@PayloadUtils.inspect_schema(Schema.INFO)
def create_student_info(payload):
    """
    建立學生資料
    """
    results = SchoolHandler.add_info(
        name=payload['name'],
        gender=payload['gender'],
        grade=payload['grade'],
        phone_number=payload['phone_number'],
    )
    return jsonify(results=results)


@app.route('/student/del', methods=['DELETE'])
def delete_info():
    """
    移除學生資料
    """
    name = request.args.get('name')
    results = SchoolHandler.delete_info(student_name=name)
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
    except KeyError:
        return 'no data exists'
    return jsonify(results=results)




