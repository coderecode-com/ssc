import json

import scrapy


class RegularRequestSpider(scrapy.Spider):
    name = 'regular_request'

    def start_requests(self):
        url = 'http://httpbin.org/post'
        form_data = {
            'username': 'admin',
            'password': 'secret'
        }
        custom_headers = {
            'user-agent': 'this is my user agent',
            "Content-Type": "application/x-www-form-urlencoded"
        }
        yield scrapy.Request(url,
                             method='POST',
                             headers=custom_headers,
                             body=json.dumps(form_data),
                             callback=self.parse
                             )

    def parse(self, response):
        self.logger.info('Successfully received the response')
        self.logger.debug(response.text)
