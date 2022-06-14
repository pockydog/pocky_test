from controllers import score_record_routes, school_routes, schedule_routes


if __name__ == "__main__":
    schedule_routes.app.run(debug=True, host='0.0.0.0', port=5000)
