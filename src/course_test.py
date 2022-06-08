import requests


class TestInfo:
    @classmethod
    def add_info(cls):
        url = 'http://127.0.0.1:5000/course/new'
        payload = {
            'name': 'Aclass',
            'classroom_id': '7',
            'is_active': True,
            'open_time': '2021-2-23 12:00:00'
        }
        response = requests.post(url=url, json=payload)
        print(response.text)

    @classmethod
    def get_info(cls):
        url = 'http://127.0.0.1:5000/course/info'
        response = requests.get(url)
        print(response.text)

    @classmethod
    def del_info(cls):
        url = 'http://127.0.0.1:5000/course/del'
        response = requests.delete(url, params={'name': 'vicky'})
        print(response.text)



if __name__ == '__main__':
    TestInfo.del_info()

