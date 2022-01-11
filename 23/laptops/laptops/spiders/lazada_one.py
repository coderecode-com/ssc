import scrapy
from scrapy_splash import SplashRequest

class LazadaOneSpider(scrapy.Spider):
    name = 'lazada_one'
    # start_urls = ['https://www.lazada.com.my/shop-laptops-gaming/?spm=a2o4k.home.cate_1_2.2.75f82e7e1Mg1X9']
    def start_requests(self):
        yield SplashRequest('https://www.lazada.com.my/shop-laptops-gaming/?spm=a2o4k.home.cate_1_2.2.75f82e7e1Mg1X9')

    def parse(self, response):
        
        for s in response.xpath('//*[@data-tracking="product-card"]'):
            yield {
                'Product' : s.xpath('./div/div/div[2]//a/text()').get(),
                'Link' : s.xpath('./div/div/div[2]//a/@href').get(),
                'Price': s.xpath('./div/div/div[2]//span[starts-with(text(),"RM")]/text()').get()
            }