from app import app
from core.classroom_hanlder import ClassroomHanlder
from flask import jsonify
from utils.payload_utils import PayloadUtils
from flask import request


@app.route('/classroom/<int:page>', methods=['GET'])
def get_classroom_info(page=None):
    """
    名稱查詢資料
    """
    per_page = request.args.get('per_page')
    name = request.args.get('name')
    result = ClassroomHanlder.get_info(name=name, per_page=per_page, page=page)
    return jsonify(result=result)


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
    name = request.args.get('name')
    results = ClassroomHanlder.del_info(name=name)
    return jsonify(results=results)


@app.route('/classroom', methods=['PUT'])
def update_classroom_info():
    """
    更新資料
    """
    payload = request.get_json()
    classroom_name = request.args.get('name')
    name = payload['name']
    location = payload['location']
    results = ClassroomHanlder.update_info(classroom_name=classroom_name, name=name, location=location)
    return jsonify(results=results)
