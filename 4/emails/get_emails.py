import scrapy


class GetEmailsSpider(scrapy.Spider):
    name = 'get_emails'
    allowed_domains = ['scrapebay.com']
    start_urls = ['https://www.scrapebay.com/email/']

    def parse(self, response):
        for s in response.css('table tbody tr'):
            yield {
                'Name' : s.css('td:nth-child(2) ::text').get(),
                'Email':s.css('td:nth-child(3) ::text').get(),
                'Thumbnail' : s.css('td:nth-child(1) img ::attr(src)').get()
            }
