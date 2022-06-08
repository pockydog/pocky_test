from app import app
from core.emergency_hanlder import EmergencyHandler
from flask import jsonify
from utils.payload_utils import PayloadUtils
from flask import request


@app.route('/emergency', methods=['GET'])
def get_emergency():
    """
    名稱查詢單筆資料
    """
    name = request.args.get('name')
    if name is None or name not in EmergencyHandler.get_info():
        results = EmergencyHandler.get_all_info()
    else:
        results = EmergencyHandler.get_emergency_info(id=id)
    return jsonify(results=results)


@app.route('/emergency/new', methods=['POST'])
@PayloadUtils.inspect_schema()
def create_info(payload):
    """
    建立關係人資料
    """
    results = EmergencyHandler().add_emergency_info(
        name=payload['name'],
        student_id=payload['student_id'],
        relationship_to_client=payload['relationship_to_client'],
        phone_number=payload['phone_number'],

    )
    return jsonify(results=results)


@app.route('/emergency/delete', methods=['DELETE'])
def delete_info():
    """
    移除關係人資料
    """
    student_id = request.args.get('student_id')
    results = EmergencyHandler.delete_emergency_info(student_id=student_id)
    return jsonify(results=results)


@app.route('/emergency/update', methods=['PUT'])
@PayloadUtils.inspect_schema()
def update_info(payload):
    """
    修改手機資料
    """
    phone_number = payload['phone_number']
    name = request.args.get('name')
    relationship = payload['relationship_to_client']
    results = EmergencyHandler.update_emergency_info(name=name, phone_number=phone_number, relationship=relationship)
    return jsonify(results=results)
