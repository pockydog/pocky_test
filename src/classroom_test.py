import requests
from faker import Faker

class GetInfo:
    @classmethod
    def get_info(cls):
        url = 'http://127.0.0.1:5000/classroom/info'
        response = requests.get(url=url)
        print(response.text)

    @classmethod
    def get_one_info(cls):
        url = 'http://127.0.0.1:5000/classroom/info/1'
        response = requests.get(url=url)
        print(response.text)

    @classmethod
    def add_info(cls):
        url = 'http://127.0.0.1:5000/classroom/new'
        fake = Faker('zh_TW')
        payload = {
            'name': f'{fake.license_plate()}',
            'location': f'{fake.address()}'
        }
        response = requests.post(url, json=payload)
        print(response.text)

    @classmethod
    def del_info(cls):
        url = 'http://127.0.0.1:5000/classroom/del'
        response = requests.delete(url, params={'name': '56-J107'})
        print(response.text)

    @classmethod
    def update_info(cls):
        url = 'http://127.0.0.1:5000/classroom/update'
        payload = {
            'name': 'vicky',
            'location': 'hoho'
        }
        response = requests.put(url, json=payload, params={'name': 'gbhnjm'})
        print(response.text)


if __name__ == '__main__':
    GetInfo.del_info()