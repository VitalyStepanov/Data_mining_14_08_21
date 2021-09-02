from pprint import pprint

import requests
from lxml import html

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/93.0.4577.63 Safari/537.36'}

response = requests.get('https://lenta.ru/', headers=header)

dom = html.fromstring(response.text)

news_name = dom.xpath('//section[@class="row b-top7-for-main js-top-seven"]//time[@class="g-time"]/text()')

#link = dom.xpahp("//")
#date_of_publication = dom.xpahp("//")
# source = dom.xpahp()


'''items = dom.xpath("//li[contains(@class,'s-item')]")

items_list = []
for item in items:
    items_data = {}
    name = item.xpath(".//h3[@class='s-item__title']/text()")
    link = item.xpath(".//h3[@class='s-item__title']/../@href")
    price = item.xpath(".//span[@class='s-item__price']//text()")
    info = item.xpath(".//span[contains(@class,'s-item__hotness')]//text()")

    items_data['name'] = name
    items_data['link'] = link
    items_data['price'] = price
    items_data['info'] = info

    items_list.append(items_data)'''

pprint(len(news_name))

