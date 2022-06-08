from app import app
from core.class_hanlder import ClassHandler
from flask import jsonify
from utils.payload_utils import PayloadUtils
from flask import request


@app.route('/class', methods=['GET'])
def get_info():
    """
    名稱查詢單筆資料
    """
    name = request.args.get('name')
    teacher_id = request.args.get('teacher_id')
    if name is None or name not in ClassHandler.get_info():
        results = ClassHandler.get_info()
    else:
        results = ClassHandler.get_one_info(name=name, teacher_id=teacher_id)
    return jsonify(results=results)


@app.route('/class/new', methods=['POST'])
@PayloadUtils.inspect_schema()
def add_info(payload):
    """
    建立資料
    """
    results = ClassHandler.add_info(
        teacher_id=payload['teacher_id'],
        course_id=payload['course_id'],
    )
    return jsonify(results=results)


@app.route('/class/del', methods=['DELETE'])
def del_info():
    """
    移除資料
    """
    teacher_id = request.args.get('teacher_id')
    results = ClassHandler.del_info(teacher_id=teacher_id)
    return jsonify(results=results)


@app.route('/class/update', methods=['PUT'])
@PayloadUtils.inspect_schema()
def update_info(payload):
    """
    修改資料
    """
    teacher_id = payload['teacher_id']
    course_id = request.args.get('course_id')
    results = ClassHandler.update_info(teacher_id=teacher_id, course_id=course_id)
    return jsonify(results=results)
