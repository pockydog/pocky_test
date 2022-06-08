import requests

class TestInfo:
    domain = 'http://127.0.0.1:5000'

    @classmethod
    def get_info(cls):
        url = f'{cls.domain}/class'
        response = requests.get(url)
        print(response.text)

    @classmethod
    def add_info(cls):
        url = f'{cls.domain}/class/new'
        payload = {
            'teacher_id': 2,
            'course_id': 6,

        }
        response = requests.post(url, json=payload)
        print(response.text)

    @classmethod
    def update_info(cls):
        url = f'{cls.domain}/class/update'
        payload = {
            'teacher_id': 2,
        }

        response = requests.put(url, json=payload, params={'course_id': 6})
        print(response.text)


    @classmethod
    def del_info(cls):
        url = f'{cls.domain}/class/del'
        response = requests.delete(url, params={'teacher_id': 2})
        print(response.text)


if __name__ == '__main__':
    TestInfo.add_info()
