from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config.from_object('config.Config')
config = app.config
db = SQLAlchemy(config)


@app.route('/')
def index():
    return 'hihi'


if __name__ == '__main__':
    app.run(debug=True)


