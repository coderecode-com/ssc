import scrapy
from price_parser import Price
from books.items import BooksItem

class BasicinfoSpider(scrapy.Spider):
    name = 'basicinfo'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/']

    def parse(self, response):
        for s in response.xpath('//ol[@class="row"]/li'):
            title = s.xpath('.//img/@alt').get()
            price_raw = s.xpath('.//*[@class="price_color"]/text()').get()
            price_object = Price.fromstring(price_raw)
            price = price_object.amount_float
            # item = BooksItem(title=title, price=price)
            item = BooksItem()
            item['title'] = title
            item['price'] = price
            
            yield item

        next_page= response.xpath('//li[@class="next"]/a/@href').get()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page))           
