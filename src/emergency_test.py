import requests


class GETINFO:

    @classmethod
    def get_one_info(cls):
        url = 'http://127.0.0.1:5000/emergency'
        response = requests.get(url=url, params={'id': 1})
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
        url = 'http://127.0.0.1:5000/emergency/delete'
        response = requests.delete(url=url, params={'student_id': 3})
        print(response.text)


    @classmethod
    def update_info(cls):
        url = 'http://127.0.0.1:5000/emergency/update'
        payload = {
            'phone_number': '09113333',
            'relationship_to_client': 'papa&mama',
        }
        response = requests.put(url=url, json=payload, params={'name': 'roro'})
        print(response.text)


if __name__ == '__main__':
     GETINFO.post_info()
    # GETINFO.delete_info()
    # GETINFO.update_info()
