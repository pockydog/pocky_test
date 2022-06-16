from flask import request
from flask import jsonify

from app import app
from core.classroom_hanlder import ClassroomHanlder
from utils.payload_utils import PayloadUtils
from const import Page


@app.route('/classroom', methods=['GET'])
@app.route('/classroom/<int:page>', methods=['GET'])
def get_classroom_info(page=1):
    """
    名稱查詢資料
    """
    per_page = request.args.get('per_page', Page.per_page, int)
    name = request.args.get('name')
    result, pagers = ClassroomHanlder.get_info(name=name, per_page=per_page, page=page)
    return jsonify(result=result, pagers=pagers)


@app.route('/classroom', methods=['POST'])
@PayloadUtils.inspect_schema()
def add_classroom_info(payload):
    """
    新增資料
    """
    results = ClassroomHanlder.add_info(
        name=payload['name'],
        location=payload['location'],
    )
    return jsonify(results=results)


@app.route('/classroom', methods=['DELETE'])
def del_classroom_info():
    """
    移除資料
    """
    id_ = request.args.get('id')
    results = ClassroomHanlder.del_info(id_=id_)
    return jsonify(results=results)


@app.route('/classroom', methods=['PUT'])
def update_classroom_info():
    """
    更新資料
    """
    payload = request.get_json()
    classroom_id = request.args.get('id')
    name = payload['name']
    location = payload['location']
    results = ClassroomHanlder.update_info(classroom_id=classroom_id, name=name, location=location)
    return jsonify(results=results)
