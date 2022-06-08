from app import create_app
from controllers import score_record_routes

app = create_app()


if __name__ == "__main__":
     score_record_routes.app.run(debug=True, host='0.0.0.0', port=5000)



