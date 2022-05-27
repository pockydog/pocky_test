import json
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm


class BigbasketParser:
    VEGETABLES = ['fresh-vegetables', 'EKXvs4-ibWQBoWMBqHNrdV9saXN0kKJuZsOiY2OoNDg5fDEzNTOpYmF0Y2hfaWR4AKJhb8KidXLComFww6JsdM0BLqNkc2rNJrShb6pwb3B1bGFyaXR5pXNyX2lkAaJkc80GuKNtcmkB']
    RICE = ['raw-rice', 'AiBd9Y-ibWQBoWMBqHNrdV9saXN0kKJuZsOiY2OrMzgxfDU4MHw4NjOpYmF0Y2hfaWR4AKJhb8KidXLComFww6JsdM0BLqNkc2rNJrShb6pwb3B1bGFyaXR5pXNyX2lkAaJkc80GuKNtcmkB']
    FRUITS = ['fresh-fruits', 'rOPJw4-ibWQBoWMBqHNrdV9saXN0kKJuZsOiY2OoNDg5fDEzNDSpYmF0Y2hfaWR4AKJhb8KidXLComFww6JsdM0BLqNkc2rNJrShb6pwb3B1bGFyaXR5pXNyX2lkAaJkc80GuKNtcmkB']
    OIL = ['edible-oils-ghee', 'SriJwY-ibWQBoWMBqHNrdV9saXN0kKJuZsOiY2OnMzgxfDM4MqliYXRjaF9pZHgAomFvwqJ1csKiYXDDomx0zQEuo2Rzas0mtKFvqnBvcHVsYXJpdHmlc3JfaWQBomRzzQa4o21yaQE=']
    SALT = ['salt-sugar-jaggery', 'DKlsC4-ibWQBoWMBqHNrdV9saXN0kKJuZsOiY2OnMzgxfDM5MaliYXRjaF9pZHgAomFvwqJ1csKiYXDDomx0zQEuo2Rzas0mtKFvqnBvcHVsYXJpdHmlc3JfaWQBomRzzQa4o21yaQE=']
    TYPE = [VEGETABLES, RICE, FRUITS, OIL, SALT]

    def __init__(self):
        self.domain ='https://www.bigbasket.com'

    def detail_api(self):
        domain = self.domain
        apis = BigbasketParser.TYPE
        api_list = list()
        api_list +=[domain + f'/custompage/sysgenpd/?type=pc&slug={api[0]}&sid={api[1]}' for api in apis]
        return api_list

    def get_product_url(self):
        urls = self.detail_api()
        url_list = list()
        for url in urls:
            headers = {
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'
            }
            response = requests.get(url=url, headers=headers)
            data = json.loads(response.text)
            urls = data['tab_info'][0]['product_info']['products']
            url_list += [self.domain + url_['absolute_url'] for url_ in urls]
        return url_list

    def get_product_info(self):
        product_list = list()
        urls = self.get_product_url()
        for url in tqdm(urls[:10]):
            headers = {
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'
            }
            response = requests.get(url=url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            info = soup.find('script')
            description = soup.find('ul')
            info = str(info).replace('<script data-react-helmet="true" type="application/ld+json">', '').replace(
                '</script>', '')
            info = json.loads(info)
            type_info = info[1]
            info = info[0]
            type_ = type_info['itemListElement'][2]['item']['name']
            type_list = ['FRESH VEGETABLES', 'RICE & RICE PRODUCTS', 'FRESH FRUITS', 'SALT, SUGAR & JAGGERY', 'EDIBLE OILS & GHEE']
            if type_ not in type_list:
                continue
            name = info['name']
            img_url = info['image']
            price = info['offers']['price']
            description = description.text
            if not (name and img_url and price and description):
                continue
            description = description.replace('\n', '').replace('\xa0', '').split('Click here')[0].split('Do not forget')[0]
            name = name.rstrip()
            img_url = img_url.replace('/s/', '/l/')
            if '.' in price:
                price = price.split('.')[0]
            info = {
                'title': name,
                'price': price,
                'img_url': img_url,
                'type': type_,
                'description': description
            }
            product_list.append(info)
        return product_list

    def exec(self):
        info_list = self.get_product_info()
        return info_list

if __name__ in '__main__':
    BigbasketParser().exec()

