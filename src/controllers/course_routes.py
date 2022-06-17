from flask import jsonify
from flask import request

from app import app
from core.course_hanlder import CourseHanlder
from utils.payload_utils import PayloadUtils
from const import Page


@app.route('/course', methods=['POST'])
@PayloadUtils.inspect_schema()
def add_course_info(payload):
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


@app.route('/course', methods=['GET'])
@app.route('/course/<int:page>', methods=['GET'])
def get_course_info(page=1):
    """
    名稱查詢單筆資料
    """
    is_active = request.args.get('is_active')
    per_page = request.args.get('per_page', Page.PER_PAGE, int)
    results, pagers = CourseHanlder.get_info(is_active=is_active, page=page, per_page=per_page)
    return jsonify(results=results, pager=pagers)


@app.route('/course', methods=['DELETE'])
def del_course_info():
    """
    移除資料
    """
    name = request.args.get('name')
    results = CourseHanlder.del_info(name=name)
    return jsonify(results=results)

