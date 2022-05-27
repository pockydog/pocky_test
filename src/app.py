from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# 設定資料庫位置，並建立 app
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:11111111@mysql_vicky_test/pockydb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

def create_app():
    return app

