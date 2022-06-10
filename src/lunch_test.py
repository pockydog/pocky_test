import requests


class Test:
    @classmethod
    def add_info(cls):
        url = 'http://127.0.0.1:5000/add'
        payload = {
            'lunch_name': 'ok'
        }
        response = requests.post(url=url, json=payload)
        print(response.text)

    @classmethod
    def get_info(cls):
        url = 'http://127.0.0.1:5000/show'
        response = requests.get(url=url)
        print(response.text)



if __name__ == '__main__':
    # Test.add_info()
    Test.get_info()