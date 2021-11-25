import scrapy
from scrapy import FormRequest


class FormRequestSpider(scrapy.Spider):
    name = 'form_request'

    def start_requests(self):
        url = 'http://httpbin.org/post'
        form_data = {
            'username': 'admin',
            'password': 'secret'
        }
        custom_headers = {
            'user-agent': 'this is my user agent'
        }
        yield FormRequest(url,
                          headers=custom_headers,
                          formdata=form_data,
                          callback=self.parse
                          )

    def parse(self, response):
        self.logger.info('Successfully received the response')
        self.logger.debug(response.text)
