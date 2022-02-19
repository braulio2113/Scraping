from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.crawler import CrawlerProcess


    
class Seminuevos(CrawlSpider):
    name = "cars"
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
        'CLOSESPIDER_ITEMCOUNT': 10
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
        model = response.xpath('//div[contains(@class,"col")]/h2[contains(@class,"m-b-none")]/text()').get()
        price = response.xpath('//meta[@itemprop="price"]/@content').get()
        price
        print(model)
        print(price)
        yield{
            'models':model,
            'prices':price
            }
        
process = CrawlerProcess({
    'FEED_FORMAT': 'csv',
    'FEED_URI': 'seminuevos.csv'
    })
process.crawl(Seminuevos)
process.start()

