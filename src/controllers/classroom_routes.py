from app import app
from core.classroom_hanlder import ClassroomHanlder
from flask import jsonify
from utils.payload_utils import PayloadUtils
from flask import request


@app.route('/classroom/info', methods=['GET'])
def get_info():
    """
    名稱查詢單筆資料
    """
    name = request.args.get('name')
    if not name:
        result = 'NO INFO'
    else:
        result = ClassroomHanlder.get_one_info(name=name)
    return jsonify(result=result)


@app.route('/classroom/new', methods=['POST'])
@PayloadUtils.inspect_schema()
def create_info(payload):
    """
    新增資料
    """
    results = ClassroomHanlder.create_info(
        name=payload['name'],
        location=payload['location'],
    )
    return jsonify(results=results)


@app.route('/classroom/del', methods=['DELETE'])
def del_info():
    """
    移除資料
    """
    name = request.args.get('name')
    results = ClassroomHanlder.del_info(name=name)
    return jsonify(results=results)


@app.route('/classroom/update', methods=['PUT'])
@PayloadUtils.inspect_schema()
def update_info(payload):
    """
    更新資料
    """
    classroom_name = request.args.get('name')
    name = payload['name']
    location = payload['location']
    results = ClassroomHanlder.update_info(classroom_name=classroom_name, name=name ,location=location)
    return jsonify(results=results)

