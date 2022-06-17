import json
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from app import db


class BigbasketExecuter:
    _CATEGORIES = {
        'fresh-vegetables': 'EKXvs4-ibWQBoWMBqHNrdV9saXN0kKJuZsOiY2OoNDg5fDEzNTOpYmF0Y2hfaWR4AKJhb8KidXLComFww6JsdM0BLqNkc2rNJrShb6pwb3B1bGFyaXR5pXNyX2lkAaJkc80GuKNtcmkB',
        'raw-rice': 'AiBd9Y-ibWQBoWMBqHNrdV9saXN0kKJuZsOiY2OrMzgxfDU4MHw4NjOpYmF0Y2hfaWR4AKJhb8KidXLComFww6JsdM0BLqNkc2rNJrShb6pwb3B1bGFyaXR5pXNyX2lkAaJkc80GuKNtcmkB',
        'fresh-fruits': 'rOPJw4-ibWQBoWMBqHNrdV9saXN0kKJuZsOiY2OoNDg5fDEzNDSpYmF0Y2hfaWR4AKJhb8KidXLComFww6JsdM0BLqNkc2rNJrShb6pwb3B1bGFyaXR5pXNyX2lkAaJkc80GuKNtcmkB',
        'edible-oils-ghee': 'SriJwY-ibWQBoWMBqHNrdV9saXN0kKJuZsOiY2OnMzgxfDM4MqliYXRjaF9pZHgAomFvwqJ1csKiYXDDomx0zQEuo2Rzas0mtKFvqnBvcHVsYXJpdHmlc3JfaWQBomRzzQa4o21yaQE=',
        'salt-sugar-jaggery': 'DKlsC4-ibWQBoWMBqHNrdV9saXN0kKJuZsOiY2OnMzgxfDM5MaliYXRjaF9pZHgAomFvwqJ1csKiYXDDomx0zQEuo2Rzas0mtKFvqnBvcHVsYXJpdHmlc3JfaWQBomRzzQa4o21yaQE=',
    }

    _HEADERS = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'
    }
    _DOMAIN = 'https://www.bigbasket.com'

    def __init__(self):
        pass

    def get_product_url(self):
        urls = [f'{self._DOMAIN}/custompage/sysgenpd/?type=pc&slug={k}&sid={v}' for k, v in self._CATEGORIES.items()]
        url_list = list()
        for url in urls:
            response = requests.get(url=url, headers=self._HEADERS)
            data = json.loads(response.text)
            urls = data['tab_info'][0]['product_info']['products']
            url_list += [self._DOMAIN + url_['absolute_url'] for url_ in urls]
        return url_list

    def exec(self, qty):
        urls = self.get_product_url()
        for url in tqdm(urls[:qty]):
            response = requests.get(url=url, headers=self._HEADERS)
            soup = BeautifulSoup(response.text, 'html.parser')
            info = soup.find('script')
            description = soup.find('ul')
            info = str(info).replace('<script data-react-helmet="true" type="application/ld+json">', '').replace(
                '</script>', '')
            info = json.loads(info)
            type_info = info[1]
            info = info[0]
            type_ = type_info['itemListElement'][2]['item']['name']
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
            into = TestInfo(
                title=name,
                price=price,
                type=type_,
                img_url=img_url,
                description=description
            )
            db.session.add(into)
        db.session.commit()

