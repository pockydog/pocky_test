from app import app
from core.schedule_hanlder import ScheduleHanlder
from flask import jsonify
from utils.payload_utils import PayloadUtils
from flask import request


@app.route('/schedule/<int:page>', methods=['GET'])
def get_info(page=None):
    """
    class_id查詢單筆資料
    """
    per_page = request.args.get('per_page', 2)
    class_id = request.args.get('class_id')
    results = ScheduleHanlder.get_info(class_id=class_id, page=page, per_page=per_page)
    return jsonify(results=results)


@app.route('/schedule', methods=['POST'])
@PayloadUtils.inspect_schema()
def add_schedule_info(payload):
    """
    建立資料
    """
    results = ScheduleHanlder.add_info(
        student_id=payload['student_id'],
        class_id=payload['class_id'],
    )
    return jsonify(results=results)


@app.route('/schedule', methods=['DELETE'])
def delete_schedule_info():
    """
    移除資料
    """
    class_id = request.args.get('class_id')
    results = ScheduleHanlder.del_info(class_id=class_id)
    return jsonify(results=results)


@app.route('/schedule', methods=['PUT'])
@PayloadUtils.inspect_schema()
def update_schedule_info(payload):
    """
    修改資料
    """
    student_id = request.args.get('student_id')
    class_id = payload['class_id']
    results = ScheduleHanlder.update_info(student_id=student_id, class_id=class_id)
    return jsonify(results=results)
