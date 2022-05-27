# from app import db
#
# class test(db.Model):
#     __tablename__ = 'role'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100))
#     # 初始化
#     def __init__(self, name):
#         self.name = name
#     # 調用內容
#     def __repr__ (self):
#         return '<>'
#
#
# db.create_all()

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
# 設定資料庫位置，並建立 app
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:11111111@mysql_vicky_test/pockydb"
db = SQLAlchemy(app)

class test(db.Model):
    __tablename__ = 'vicky'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    @classmethod
    def sign_in(cls, name):
        name = cls.name
        conditions = [
            test.name == name,
        ]
        user = test.query.filter(
            *conditions
        ).first()
        db.session.add(user)
        return {
            'id': user.id,
            'name': user.name,
        }

    @app.route('/sign-in')
    def sign_in(cls):
        """
        登入
        """
        results = cls.test()
        print(results)
        return jsonify(results=results)

    if __name__ == "__main__":
        sign_in()
    #     app.run(debug=True, host='0.0.0.0', port=5000)
