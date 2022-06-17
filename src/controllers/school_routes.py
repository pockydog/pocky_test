from flask import request
from flask import jsonify

from app import app
from core.school_hanlder import SchoolHandler
from utils.payload_utils import PayloadUtils
from utils.school_schema import Schema
from const import Page


@app.route('/student', methods=['GET'])
@app.route('/student/<int:page>', methods=['GET'])
def get_student_info(page=1):
    """
    名稱查詢單筆資料
    """
    name = request.args.get('name')
    per_page = request.args.get('per_page', Page.PER_PAGE, int)
    results, pagers = SchoolHandler.get_info(name=name, page=page, per_page=per_page)
    return jsonify(results=results, pagers=pagers)


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


@app.route('/student', methods=['DELETE'])
def delete_info():
    """
    移除學生資料
    """
    name = request.args.get('name')
    results = SchoolHandler.delete_info(student_name=name)
    return jsonify(results=results)


@app.route('/student', methods=['PUT'])
@PayloadUtils.inspect_schema()
def update_info(payload):
    """
    修改學生資料
    """
    results = SchoolHandler.update_info(student_name=request.args.get('name'),
                                        phone_number=payload['phone_number'])
    return jsonify(results=results)
