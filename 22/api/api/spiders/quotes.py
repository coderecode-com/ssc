import scrapy
from scrapy.shell import inspect_response
import json

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['https://quotes.toscrape.com/js/']

    def parse(self, response):
        # inspect_response(response, self)
        raw_data = response.xpath('normalize-space(//script[not(@src)]/text())').get()
        end_position = raw_data.find('; for (var i in data)')
        start_postion = len('var data =')
        sliced_data = raw_data[start_postion:end_position]
        data = json.loads(sliced_data)
        for item in data:
            yield item