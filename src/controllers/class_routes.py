from flask import jsonify
from flask import request

from app import app
from core.class_hanlder import ClassHandler
from utils.payload_utils import PayloadUtils
from const import Page


@app.route('/class', methods=['GET'])
@app.route('/class/<int:page>', methods=['GET'])
def get_class_info(page=1):
    """
    名稱查詢單筆資料
    """
    teacher_id = request.args.get('teacher_id')
    per_page = request.args.get('per_page', Page.PER_PAGE, int)
    results, pager = ClassHandler.get_info(teacher_id=teacher_id, page=page, per_page=per_page)
    return jsonify(results=results, pager=pager)


@app.route('/class', methods=['POST'])
@PayloadUtils.inspect_schema()
def add_class_info(payload):
    """
    建立資料
    """
    results = ClassHandler.add_info(
        teacher_id=payload['teacher_id'],
        course_id=payload['course_id'],
    )
    return jsonify(results=results)


@app.route('/class', methods=['DELETE'])
def del_class_info():
    """
    移除資料
    """
    class_id = request.args.get('id')
    results = ClassHandler.del_info(class_id=class_id)
    return jsonify(results=results)


@app.route('/class', methods=['PUT'])
@PayloadUtils.inspect_schema()
def update_class_info(payload):
    """
    修改資料
    """
    test = '1'
    teacher_id = payload['teacher_id']
    course_id = request.args.get('course_id')
    results = ClassHandler.update_info(teacher_id=teacher_id, course_id=course_id)
    return jsonify(results=results)

