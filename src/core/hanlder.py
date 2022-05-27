import sys
from app import db

from utils.models import Test, TestInfo


class UserHandler:

    @classmethod
    def get_info(cls):
        test = Test
        user = db.session.query(test.id, test.name, test.age, test.dog_name, test.dog_age).all()
        result_list = list()
        for id, name, age, dog_name, dog_age in user:
            result = {
                'id': id,
                'name': name,
                'age': age,
                'dog_name': dog_name,
                'dog_age': dog_age
            }
            result_list.append(result)

        return result_list


    @classmethod
    def get_test_info(cls):
        user = db.session.execute("select * from test_info").fetchall()
        # user = db.session.query(TestInfo.id, TestInfo).all()
        result_list = list()
        for id, title, price, type, img_url, description in user:
            result = {
                'id': id,
                'title': title,
                'price': price,
                'type': type,
                'img_url': img_url,
                'description': description
            }
            result_list.append(result)

        return result_list


    @classmethod
    def get_teacher_info(cls):
        results = TestInfo.query.filter_by(id=3).first()
        return results

