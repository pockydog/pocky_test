from app import create_app
from controllers import emergency_routes
import requests

app = create_app()


if __name__ == "__main__":
#     # user_routes.app.run(debug=True, host='0.0.0.0', port=5000)
    emergency_routes.app.run(debug=True, host='0.0.0.0', port=5000)



