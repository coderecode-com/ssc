import scrapy
from price_parser import Price

class BasicinfoSpider(scrapy.Spider):
    name = 'books_loop'
    allowed_domains = ['books.toscrape.com']
    # start_urls = ['https://books.toscrape.com/']
    def start_requests(self):
        url = 'https://books.toscrape.com/catalogue/page-{}.html'
        for i in range(1, 51):
            yield scrapy.Request(url.format(i))

    def parse(self, response):
        for s in response.xpath('//ol[@class="row"]/li'):
            title = s.xpath('.//img/@alt').get()
            price_raw = s.xpath('.//*[@class="price_color"]/text()').get()
            price_object = Price.fromstring(price_raw)
            price = price_object.amount_float
            
            yield {
                'Title' :title, 
                'Price':price
            }
