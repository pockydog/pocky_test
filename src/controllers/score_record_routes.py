from app import app
from core.score_record_hanlder import ScoreRecordHandler
from flask import jsonify
from utils.payload_utils import PayloadUtils
from flask import request


@app.route('/score/<int:page>', methods=['GET'])
def get_score_student(page=None):
    """
    名稱查詢單筆資料
    """
    schedule_id = request.args.get('schedule_id')
    per_page = request.args.get('per_page')
    results = ScoreRecordHandler.get_info(schedule_id=schedule_id, page=page, per_page=per_page)
    return jsonify(results=results)


@app.route('/score', methods=['POST'])
@PayloadUtils.inspect_schema()
def add_score_info(payload):
    """
    建立資料
    """
    results = ScoreRecordHandler.add_info(
        score=payload['score'],
        schedule_id=payload['schedule_id'],
    )
    return jsonify(results=results)


@app.route('/score', methods=['DELETE'])
def del_score_info():
    """
    移除資料
    """
    schedule_id = request.args.get('schedule_id')
    results = ScoreRecordHandler.del_info(schedule_id=schedule_id)
    return jsonify(results=results)


@app.route('/score', methods=['PUT'])
@PayloadUtils.inspect_schema()
def update_score_info(payload):
    """
    修改資料
    """
    schedule_id = request.args.get('schedule_id')
    score = payload['score']
    try:
        results = ScoreRecordHandler.update_info(schedule_id=schedule_id, score=score)
    except KeyError:
        return 'no data exists'
    return jsonify(results=results)
