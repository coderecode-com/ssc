import scrapy
from scrapy.shell import inspect_response

class QuotesSpider(scrapy.Spider):
    name = 'quotes'

    start_urls = ['https://quotes.toscrape.com/api/quotes?page=1']

    def parse(self, response):
        data = response.json()
        quotes = data.get('quotes')
