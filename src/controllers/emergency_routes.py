from app import app
from core.emergency_hanlder import EmergencyHandler
from flask import jsonify
from utils.payload_utils import PayloadUtils
from flask import request


@app.route('/emergency', methods=['GET'])
def get_emergency_info():
    """
    名稱查詢單筆資料
    """
    student_id = request.args.get('student_id')
    results = EmergencyHandler.get_info(student_id=student_id)
    return jsonify(results=results)


@app.route('/emergency', methods=['POST'])
@PayloadUtils.inspect_schema()
def create_emergency_info(payload):
    """
    建立關係人資料
    """
    results = EmergencyHandler.add_info(
        name=payload['name'],
        student_id=payload['student_id'],
        relationship_to_client=payload['relationship_to_client'],
        phone_number=payload['phone_number'],
    )
    return jsonify(results=results)


@app.route('/emergency/<int:student_id>', methods=['DELETE'])
def delete_emergency_info(student_id):
    """
    移除關係人資料
    """
    results = EmergencyHandler.delete_info(student_id=student_id)
    return jsonify(results=results)


@app.route('/emergency', methods=['PUT'])
@PayloadUtils.inspect_schema()
def update_emergency_info(payload):
    """
    修改手機資料
    """
    phone_number = payload['phone_number']
    name = request.args.get('name')
    relationship = payload['relationship_to_client']

    results = EmergencyHandler.update_info(name=name, phone_number=phone_number, relationship=relationship)
    return jsonify(results=results)
