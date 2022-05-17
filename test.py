import sqlalchemy as db


def demo():
    url = 'mysql+pymysql://root:11111111@localhost:8000/pockydb'
    engine = db.create_engine(url, pool_recycle=3600)
    connection = engine.connect()
    metadata = db.MetaData()
    table = db.Table('pocky_food', metadata, autoload=True, autoload_with=engine)
    query = db.insert(table).values(food_type='candy')
    # connection.execute(query)

    query = db.insert(table)
    values = [
        {'food_type': 'pork'},
        {'food_type': 'vege'},
    ]
    # connection.execute(query, values)

    query =db.select([table]).order_by(db.desc(table.columns.id)).limit(1)
    rows = connection.execute(query).fetchall()
    for row in rows:
        print(row.id, row.food_type)

    query =db.update(table).values(food_type='new_beef').where(table.columns.id == 1)
    # connection.execute(query)

    query = db.delete(table).where(table.columns.food_type == 'vege')
    connection.execute(query)
    return


if __name__ == '__main__':
    demo()
