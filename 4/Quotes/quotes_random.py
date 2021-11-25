import scrapy


class QuotesRandomSpider(scrapy.Spider):
    name = 'quotes_random'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/random']

    def parse(self, response):
        quote_text = response.css('span.text ::text').get()
        author = response.css('.author ::text').get()
        tags = response.css('a.tag ::text').getall()
        item = {}
        item['Quote'] = quote_text
        item['Author'] = author
        item['Tags'] = tags
        
        yield item 