import sys
sys.path.append('/app')
sys.path.append('/app//modles')
print("\n".join(sys.path))

from utils.modles import test, Test_info
from app import db


class UserHandler:

    @classmethod
    def get_info(cls):
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
        # user = db.session.query(Test_info.id, Test_info).all()
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
        print(result_list)

        return result_list


    @classmethod
    def get_teacher_info(cls):
        results = Test_info.query.filter_by(id=3).first()
        return results


if __name__ =='__main__':
    UserHandler.get_teacher_info()

