from app import app
from core.classroom_hanlder import ClassroomHanlder
from flask import jsonify
from utils.payload_utils import PayloadUtils
from flask import request


@app.route('/classroom/info', methods=['GET'])
def get_info():
    result = ClassroomHanlder.get_info()
    return jsonify(result=result)


@app.route('/classroom/new', methods=['POST'])
@PayloadUtils.inspect_schema()
def create_info(payload):
    results = ClassroomHanlder.create_info(
        name=payload['name'],
        location=payload['location']
    )
    return jsonify(results=results)


@app.route('/classroom/del', methods=['DELETE'])
def del_info():
    name = request.args.get('name')
    results = ClassroomHanlder.del_info(name=name)
    return jsonify(results=results)


@app.route('/classroom/update', methods=['PUT'])
@PayloadUtils.inspect_schema()
def update_info(payload):
    classroom_name = request.args.get('name')
    name=payload['name']
    location = payload['location']
    results = ClassroomHanlder.update_info(classroom_name=classroom_name, name=name ,location=location)
    return jsonify(results=results)


