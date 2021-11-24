import scrapy
import json


class PostRequestSpider(scrapy.Spider):
    name = 'post_request'

    def start_requests(self):
        url = "http://httpbin.org/post"
        headers = {
            'accept': 'application/json'
        }
        data = {'name': 'upendra'}

        yield scrapy.Request(url=url, method='POST',
                             headers=headers,
                             body=json.dumps(data),
                             callback=self.parse)

    def parse(self, response):
        print(response.text)
