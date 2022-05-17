import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DB_NAME = 'pockydb'

    SQLALCHEMY_BINDS = {
        DB_NAME: 'mysql+pymysql://{usr}:{pwd}@{host}:{port}/{db}'.format(
            usr=os.environ['MYSQL_USER'],
            pwd=os.environ['MYSQL_PASSWORD'],
            host=os.environ['MYSQL_HOST'],
            port=os.environ['MYSQL_PORT'],
            db=DB_NAME
        ),
    }





