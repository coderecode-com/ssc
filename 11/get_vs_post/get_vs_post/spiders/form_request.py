import scrapy
import json
from scrapy import FormRequest


class PostRequestSpider(scrapy.Spider):
    name = 'form_request'

    def start_requests(self):
        url = "http://httpbin.org/post"
        headers = {
            'accept': 'application/json'
        }
        data = {'user': 'upendra',
                'password':'secret'}

        yield FormRequest(url=url,
                          headers=headers,
                          formdata=data,
                          callback=self.parse)

    def parse(self, response):
        print(response.text)
