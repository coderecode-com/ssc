import scrapy


class AllQuotesSpider(scrapy.Spider):
    name = 'all_quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        for s in response.css('.quote'):
            quote_text = s.css('span.text ::text').get()
            author = s.css('small.author ::text').get()
            tags = s.css('.tag ::text').getall()
            yield {
                'Quote' : quote_text,
                'Author': author,
                'Tags' : tags
            }
            
