from sqlalchemy import create_engine, MetaData, Table, Integer, String, DATETIME, Column
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask import jsonify
from datetime import datetime


db = SQLAlchemy()
app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:11111111@mysql_vicky_test/pockydb"
db = SQLAlchemy(app)

meta = MetaData()
db = 'mysql+pymysql://root:11111111@mysql_vicky_test/pockydb'
user = Table('user', meta,
             Column('id', Integer(), primary_key=True),
             Column('name', String(100), nullable=False),
             Column('dog_name', String(100), nullable=False),
             Column('create_date', DATETIME(), default=datetime.now, nullable=False),
             Column('update_on', DATETIME(), default=datetime.now, onupdate=datetime.now, nullable=False)
             )
engine = create_engine(db)
meta.create_all(engine)
info = user.insert().values(
    name='mama',
    dog_name='me',
)
# result = engine.connect().execute(info)
info2 = user.insert()
values = [
    {'name': 'vicky_chen', 'dog_name': 'pockydog'},
    {'name': 'roro', 'dog_name': 'cogi'},
    {'name': 'evn', 'dog_name': 'bugu'},
    {'name': 'shan', 'dog_name': 'kilala'}
]
# result = engine.connect().execute(info2, values)

# query = user.update().values(dog_name='pocky').where(user.columns.name == 'vicky_chen')
# result = engine.connect().execute(query)

# query = user.delete().where(user.columns.dog_name == 'cogi')
# result = engine.connect().execute(query)

# query =user.select().order_by(user.columns.id).limit(10)
# rows = engine.connect().execute(query).fetchall()
# # for row in rows:
# #     print(row.id, row.name)
query =user.select()
rows = engine.connect().execute(query).fetchall()
print(rows)
for i in rows:




if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)