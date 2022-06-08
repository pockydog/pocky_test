from app import app
from core.schedule_hanlder import ScheduleHanlder
from flask import jsonify
from utils.payload_utils import PayloadUtils
from flask import request


@app.route('/schedule', methods=['GET'])
def get_info():
    """
    id查詢單筆資料
    """
    class_id = request.args.get('class_id')
    if class_id is None or class_id not in ScheduleHanlder.get_all_info():
        results = ScheduleHanlder.get_all_info()
    else:
        results = ScheduleHanlder.get_info(class_id=class_id)
    return jsonify(results=results)


@app.route('/schedule/new', methods=['POST'])
@PayloadUtils.inspect_schema()
def add_info(payload):
    """
    建立資料
    """
    results = ScheduleHanlder.add_info(
        student_id=payload['student_id'],
        class_id=payload['class_id'],
    )
    return jsonify(results=results)


@app.route('/schedule/delete', methods=['DELETE'])
def delete_info():
    """
    移除資料
    """
    class_id = request.args.get('class_id')
    results = ScheduleHanlder.del_info(class_id=class_id)
    return jsonify(results=results)


@app.route('/schedule/update', methods=['PUT'])
@PayloadUtils.inspect_schema()
def update_info(payload):
    """
    修改資料
    """
    student_id = request.args.get('student_id')
    class_id = payload['class_id']
    results = ScheduleHanlder.update_info(student_id=student_id, class_id=class_id)
    return jsonify(results=results)

