import requests
from lxml import etree

pais = 'ar/sodimac-ar'

url = f'https://www.sodimac.com.{pais}/product'


sku_tuple = ('2985977', '8723974', '2006707', '3225461', '3225453', '2245159', '1092138', '8756570', '8756546', '2249626', '1837273', '8889384', '8889341', '8889392', '8889368', '8889325', '8889376', '888935X', '8889252', '8889260', '8889295', '8889317', '8889279', '8889309', '8889287', '8889422', '8889414', '8889406', '3229645')

for sku in sku_tuple:
    url_with_sku = f'{url}/{sku}/'
    req = requests.get(url_with_sku, auth=('user', 'pass'))
    req = req.text
    tree = etree.HTML(req)
    # print(req)
    expression = '//div[@class="jsx-875689833 main"]//div[@class="jsx-4095377833 product-basic-info"]//div[@class="jsx-2016778456 primary"]//span[@class="jsx-2016778456"]/text()'
    verify = tree.xpath(expression)

    if len(verify) > 0:
        print(f'{sku} in web')
    else:
        print(f'{sku} not in web')