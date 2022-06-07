from app import app
from core.hanlder import UserHandler
from flask import jsonify


@app.route('/')
def get_something():
    """
    test_data
    """
    results = UserHandler.get_info()
    return jsonify(results=results)

@app.route('/get-info')
def get_some():
    """
    test_info
    """
    results = UserHandler.get_teacher_info()
    if not results:
        return 'testt'
    return jsonify(results=results)





