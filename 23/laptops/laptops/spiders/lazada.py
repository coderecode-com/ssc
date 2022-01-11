import scrapy
from scrapy_splash import SplashRequest


class LazadaSpider(scrapy.Spider):
    name = 'lazada'
    # start_urls = ['https://www.lazada.com.my/shop-laptops-gaming/?spm=a2o4k.home.cate_1_2.2.75f82e7e1Mg1X9']

    def start_requests(self):
        yield SplashRequest('https://www.lazada.com.my/shop-laptops-gaming/?spm=a2o4k.home.cate_1_2.2.75f82e7e1Mg1X9')

    def parse(self, response):

        for s in response.xpath('//*[@data-tracking="product-card"]'):
            link = s.xpath('./div/div/div[2]//a/@href').get()
            link = response.urljoin(link)
            yield scrapy.Request(link, callback=self.product_details)

    def product_details(self, response):
        yield {
            'Product': response.xpath('//h1[@class="pdp-mod-product-badge-title"]/text()').get(),
            'Price': response.xpath('//div[@class="pdp-product-price"]/span/text()').get(),
            'Link': response.url
        }
