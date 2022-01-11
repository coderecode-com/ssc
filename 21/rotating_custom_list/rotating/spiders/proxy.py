import scrapy


class ProxySpider(scrapy.Spider):
    name = 'proxy'

    def start_requests(self):
        for _ in range(5):
            yield scrapy.Request('http://httpbin.org/ip',
                                 dont_filter=True
                                 )

    def parse(self, response):
        self.logger.info(response.json())
