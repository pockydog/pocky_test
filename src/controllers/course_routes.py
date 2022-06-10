from app import app
from core.course_hanlder import CourseHanlder
from flask import jsonify
from utils.payload_utils import PayloadUtils
from flask import request


@app.route('/course/new', methods=['POST'])
@PayloadUtils.inspect_schema()
def add_info(payload):
    """
    新增資料
    """
    results = CourseHanlder.add_info(
        name=payload['name'],
        classroom_id=payload['classroom_id'],
        is_active=payload['is_active'],
        open_time=payload['open_time']
    )
    return jsonify(results=results)


@app.route('/course/info', methods=['GET'])
def get_info():
    """
    名稱查詢單筆資料
    """
    results = CourseHanlder.get_info()
    return jsonify(results=results)


@app.route('/course/del', methods=['DELETE'])
def del_info():
    """
    移除資料
    """
    name = request.args.get('name')
    results = CourseHanlder.del_info(name=name)
    return jsonify(results=results)

