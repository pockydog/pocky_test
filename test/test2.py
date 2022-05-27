from sqlalchemy import create_engine, MetaData, Table, Integer, String, DATETIME, Column
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask import jsonify
from datetime import datetime
import json

db = SQLAlchemy()
app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:11111111@mysql_vicky_test/pockydb"
db = SQLAlchemy(app)

meta = MetaData()
db_ = 'mysql+pymysql://root:11111111@mysql_vicky_test/pockydb'

user = Table('user', meta,
             Column('id', Integer(), primary_key=True),
             Column('name', String(100), nullable=False),
             Column('dog_name', String(100), nullable=False),
             Column('create_date', DATETIME(), default=datetime.now, nullable=False),
             Column('update_on', DATETIME(), default=datetime.now, onupdate=datetime.now, nullable=False)
             )

engine = create_engine(db_)
meta.create_all(engine)

user_list = db.session.query(user).all()
row2dict = lambda r: dict(r.items())

# for i in user_list:
#     print(i)

# print(user_list)



@app.route('/')
def username():
    return row2dict


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)