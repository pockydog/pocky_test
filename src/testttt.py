import json
import requests
import time
from bs4 import BeautifulSoup
import re
from tqdm import tqdm
class DarazParser:
    def __init__(self):
        self.domain ='https://www.daraz.pk/rice/?spm=a2a0e.searchlistcategory.cate_1_4.9.a31652f2wDUgrW'

    def get_product_url(self):
        url = self.domain
        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'
        }
        time.sleep(20)
        response = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        datas = None
        infos = soup.find_all('script')
        for info in infos:
            if 'window.pageData' in info.text:
                info = str(info).replace('<script>window.pageData=', '').replace('</script>', '')
                datas = json.loads(info)
        url = [data['productUrl'] for data in datas['mods']['listItems']]
        return url

    def get_product_info(self):
        # urls = f'https:{self.get_product_url()}'
        url ='https://www.daraz.pk/products/5-kg-i100430092-s1245753137.html?spm=a2a0e.searchlistcategory.list.3.61357fa4NH8EoL&search=1'
        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'
        }
        time.sleep(20)
        response = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        script_items = soup.find_all('script')
        data = None
        for script_item in script_items:
            if 'app.run' in script_item.text:
                data = re.compile(r'app.run\((.*?)\);\n')
                data = data.search(str(script_item))
                data = json.loads(data.group(1))
        infos = data['data']['root']['fields']
        name = infos['htmlRender']['msiteShare']['title']
        info_ = infos['skuInfos']['0']
        price = info_['price']['salePrice']['value']
        type_ = info_['dataLayer']['pdt_category']
        title_ = infos['specifications']['1245753137']['features']
        img_url = infos['skuGalleries']['0']
        print(img_url)
        print(price)
        print(title_)
        print(type_)



if __name__ == '__main__':
    DarazParser().get_product_info()


