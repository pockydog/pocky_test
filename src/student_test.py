import requests


class GETINFO:
    @classmethod
    def get_info(cls):
        url = 'http://127.0.0.1:5000/emergency'
        response = requests.get(url=url)
        print(response.text)

    @classmethod
    def get_one_info(cls):
        url = 'http://127.0.0.1:5000/emergency'
        response = requests.get(url=url, params={'id': 1})
        print(response.text)

    @classmethod
    def post_info(cls):
        url = 'http://127.0.0.1:5000/student/new'
        payload = {
            'name': 'pocky',
            'gender': 1,
            'grade': 2,
            'phone_number': 98765432,
        }
        response = requests.post(url=url, json=payload)
        print(response.text)

    @classmethod
    def post_info(cls):
        url = 'http://127.0.0.1:5000/emergency/new'
        payload = {
            'name': 'pockypapa',
            'student_id': 1,
            'phone_number': 98765432,
            'relationship_to_client': 'pa_pa',
        }
        response = requests.post(url=url, json=payload)
        print(response.text)

    @classmethod
    def delete_info(cls):
        url = 'http://127.0.0.1:5000/delete-info'
        response = requests.delete(url=url, params={'name': 'vicky'})
        print(response.text)

    @classmethod
    def create_test(cls):
        url = 'http://127.0.0.1:5000/student/test'
        payload = {
            'name': 'podog',
            'gender': 2,
            'grade': 2,
            'phone_number': '98765432',
        }
        response = requests.post(url=url, json=payload)
        print(response.text)

    @classmethod
    def update_info(cls):
        url = 'http://127.0.0.1:5000/student/update'
        payload = {
            'phone_number': '0911',
        }
        response = requests.put(url=url, json=payload, params={'name': 'vicky'})
        print(response.text)



if __name__ == '__main__':
    # GETINFO.create_test()
    # GETINFO.get_one_info()
    GETINFO.post_info()
    # GETINFO.get_one_info()
    # GETINFO.update_info()



