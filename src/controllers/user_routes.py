import sys
sys.path.append('/app')
sys.path.append('/app//hanlder')

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
    results = UserHandler.get_test_info()
    return jsonify(results=results)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

