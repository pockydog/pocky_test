import requests


class GETINFO:

    @classmethod
    def get_one_info(cls):
        url = 'http://127.0.0.1:5000/schedule'
        response = requests.get(url=url, params={'class_id': 6})
        print(response.text)

    @classmethod
    def post_info(cls):
        url = 'http://127.0.0.1:5000/schedule/new'
        payload = {
            'student_id': 1,
            'class_id': 2,
        }
        response = requests.post(url=url, json=payload)
        print(response.text)

    @classmethod
    def delete_info(cls):
        url = 'http://127.0.0.1:5000/schedule/delete'
        response = requests.delete(url=url, params={'class_id': 6})
        print(response.text)


    @classmethod
    def update_info(cls):
        url = 'http://127.0.0.1:5000/schedule/update'
        payload = {
            'class_id': 6,
        }
        response = requests.put(url=url, json=payload, params={'student_id': 2})
        print(response.text)


if __name__ == '__main__':
    # GETINFO.post_info()
    GETINFO.update_info()
