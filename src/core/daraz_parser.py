import json
import re
import time
from random import randint
from tqdm import tqdm

import requests
from bs4 import BeautifulSoup

class DarazParser:
    _DOMAIN = 'https://www.daraz.pk'
    _PRODUCT_LIST = {
        'RICE' : 'rice',
        'COOKING_OIL' : 'cooking-oils',
        'POTATOES' : 'buy-fresh-potatoes',
            }
    _HEADERS = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'
    }

    @staticmethod
    def _find_script_item(items, word):
        data = None
        for item in items:
            if word in str(item):
                data = item
                break
        return data

    @classmethod
    def testt(cls):
        url = 'https://www.daraz.pk/products/dfresh-shakarkandi-sweet-potato-half-kg-i200784557.html'
        response = requests.get(url=url, headers=cls._HEADERS)
        print(response.text)
        # soup = BeautifulSoup(response.text, 'html.parser')
        # type_list = soup.find_all('a', {'class': 'breadcrumb_item_anchor'})
        # print(type_list)
        # type_ = [i.text.replace('\n', '') for i in type_list].pop()
        # description = soup.find_all('script')
        # description = cls._find_script_item(items=description, word='app/pc')
        # data = re.compile(r'app.run\((.*?)\);\n')
        # data = data.search(str(description))
        # data = json.loads(data.group(1))
        # product_id = data['data']['root']['fields']['specifications']
        # product = list(product_id.keys())[0]
        # product_id = product_id[product]['features']
        # description = ''.join(f'{k}: {v}' for k, v in product_id.items())
        # return description, type_

    # @classmethod
    # def test(cls):
    #     urls = cls._PRODUCT_LIST
    #     urls = list(urls.values())
    #     product_list = list()
    #     for url in tqdm(urls):
    #         url = f'{cls._DOMAIN}/{url}'
    #         response = requests.get(url=url, headers=cls._HEADERS)
    #         soup = BeautifulSoup(response.text, 'html.parser')
    #         print(soup)
    #         script_items = soup.find_all('script')
    #         script_item = cls._find_script_item(items=script_items, word='window.pageData={"mods":')
    #         data = str(script_item).replace('<script>', '').replace('</script>', '').replace('window.pageData=', '')
    #         data = json.loads(data)
    #         datas = data['mods']['listItems']
    #         for data in tqdm(datas):
    #             url_ = data['productUrl']
    #             url_ = f'https:{url_}'
    #             type_, description = cls.get_type_info(url=url_)
    #             name = data['name']
    #             img_url = data['image']
    #             price = data['price']
    #             price = price.split('.')[0]
    #             result = {
    #                 'title': name,
    #                 'img_url': img_url,
    #                 'price': price,
    #                 'type': type_,
    #                 'description': description
    #             }
    #             product_list.append(result)
    #     return product_list



















