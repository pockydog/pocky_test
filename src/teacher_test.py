import requests
from faker import Faker


class GETINFO:
    @classmethod
    def get_info(cls):
        url = 'http://127.0.0.1:5000/teacher'
        response = requests.get(url=url)
        print(response.text)

    @classmethod
    def add_info(cls):
        fake = Faker()
        url = 'http://127.0.0.1:5000/teacher/new'
        payload = {
            'name': f'{ fake.name()}',
            'gender': 1,
            'phone_number': '0987654321',
        }
        response = requests.post(url=url, json=payload)
        print(response.text)

    @classmethod
    def delete_info(cls):
        url = 'http://127.0.0.1:5000/teacher/delete'
        response = requests.delete(url=url, params={'name': 'teacher0'})
        print(response.text)

    @classmethod
    def update_info(cls):
        url = 'http://127.0.0.1:5000/teacher/update'
        payload = {
            'gender': True,
            'phone_number': '0988888888',
        }
        response = requests.put(url, json=payload, params={'name': 'teacher1'})
        print(response.text)





if __name__ == '__main__':
    # GETINFO.get_info()
    GETINFO.update_info()
