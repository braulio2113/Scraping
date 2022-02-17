from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader


class Car(Item):
    model = Field()
    price = Field()
    
class Vivanuncios(CrawlSpider):
    name = "Hoteles"
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
        'CLOSESPIDER_ITEMCOUNT': 50
    }
    start_urls = ['https://www.seminuevos.com/usados/-/autos?type_autos_moderated=moderated']
    
    download_delay = 2
    
    rules = (
        Rule(# Horizontal
            LinkExtractor(
                allow = r'page='
                ), follow = True
            ),
        Rule(# Vertical
            LinkExtractor(
                allow = r'/vehicle/'
                ), follow = True, callback = 'parse_item'
            ),
        )
    
    def parse_item(self, response):
        sel = Selector(response)
        item = ItemLoader(Car(), sel)
        
        item.add_xpath('model', '//div[contains(@class,"col")]/h2[contains(@class,"m-b-none")]/text()')
        item.add_xpath('price', '//meta[@itemprop="price"]/@content' , MapCompose(lambda i: i.replace('.', ',')))
        yield item.load_item()
        
        
#scrapy runspider Seminuevos(Scrapy_V).py -o seminuevos.csv -t csv
