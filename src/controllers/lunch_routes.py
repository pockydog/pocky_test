from core.lunch_hanlder import Test
from flask import jsonify
from utils.payload_utils import PayloadUtils
from app import app


@app.route('/add', methods=['POST'])
@PayloadUtils.inspect_schema()
def add_info(payload):
    results = Test.add_info(
        lunch_name=payload['lunch_name']
    )
    return jsonify(results=results)


@app.route('/show', methods=['GET'])
def get_info():
    results = Test.get_info()
    return jsonify(results=results)
