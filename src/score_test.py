import requests


class GETINFO:

    @classmethod
    def get_one_info(cls):
        url = 'http://127.0.0.1:5000/score'
        response = requests.get(url=url, params={'class_id': 6})
        print(response.text)

    @classmethod
    def post_info(cls):
        url = 'http://127.0.0.1:5000/score/new'
        payload = {
            'score': 100,
            'schedule_id': 6,
        }
        response = requests.post(url=url, json=payload)
        print(response.text)

    @classmethod
    def delete_info(cls):
        url = 'http://127.0.0.1:5000/score/del'
        response = requests.delete(url=url, params={'schedule_id': 6})
        print(response.text)

    #
    @classmethod
    def update_info(cls):
        url = 'http://127.0.0.1:5000/score/update'
        payload = {
            'score': 60,
        }
        response = requests.put(url=url, json=payload, params={'schedule_id': 9})
        print(response.text)


if __name__ == '__main__':
    # GETINFO.post_info()
    GETINFO.delete_info()
