import scrapy
from scrapy.loader import ItemLoader

from books.items import BooksItem


class BookLoaderSpider(scrapy.Spider):
    name = 'book_loader'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/']

    def parse(self, response):
        # inspect_response(response, self)
        for s in response.xpath('//ol[@class="row"]/li'):
            loader = ItemLoader(item=BooksItem(), response=response, selector=s)

            loader.add_xpath('title', './/img/@alt')
            loader.add_xpath('price', './/*[@class="price_color"]/text()')
            loader.add_xpath('currency', './/*[@class="price_color"]/text()')
            loader.add_xpath('available', './/*[@class="instock availability"]')
            loader.add_xpath('in_stock', './/*[@class="instock availability"]/text()')
            yield loader.load_item()

        next_page = response.xpath('//li[@class="next"]/a/@href').get()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page))
