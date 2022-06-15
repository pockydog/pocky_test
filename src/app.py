from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config



app = Flask(__name__)
# 設定資料庫位置，並建立 app
config = Config()
app.config.from_object(config)
db = SQLAlchemy(app)

from controllers import *


def create_app():
    return app

