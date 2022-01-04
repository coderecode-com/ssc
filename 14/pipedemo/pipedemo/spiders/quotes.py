import scrapy

from pipedemo.items import QuoteItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/']
    
    custom_settings = {
        'ITEM_PIPELINES': {
            'pipedemo.pipelines.QuotesPipeline': 300,
        }
    }

    def parse(self, response):
        for s in response.css('.quote'):
            item = QuoteItem()

            item['Quote'] = s.css('span.text ::text').get()
            item['Author'] = s.css('small.author ::text').get()
            item['Tags'] = s.css('.tag ::text').getall()

            yield item
