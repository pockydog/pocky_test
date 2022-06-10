from app import create_app
from controllers import lunch_routes, emergency_routes
from core.lunch_hanlder import Test
from core.score_record_hanlder import ScoreRecord

app = create_app()

if __name__ == "__main__":
     emergency_routes.app.run(debug=True, host='0.0.0.0', port=5000)
     # lunch_routes.app.run(debug=True, host='0.0.0.0', port=5000)