from sqlalchemy import create_engine, MetaData, Table,Integer, String, DATETIME, Column
from datetime import datetime


meta = MetaData()
db = 'mysql+pymysql://root:11111111@localhost:8000/pockydb'
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

# query =user.update().values(dog_name='pocky').where(user.columns.name == 'vicky_chen')
# result = engine.connect().execute(query)

# query = user.delete().where(user.columns.dog_name == 'cogi')
# result = engine.connect().execute(query)

# query =user.select().order_by(user.columns.id).limit(10)
# rows = engine.connect().execute(query).fetchall()
# for row in rows:
#     print(row.id, row.name)