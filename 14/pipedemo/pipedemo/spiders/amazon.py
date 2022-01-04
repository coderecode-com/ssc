import scrapy

from pipedemo.items import AmazonItem


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/s?k=laptop']
    custom_settings = {
        'ITEM_PIPELINES':{
            'pipedemo.pipelines.AmazonPipeline': 300,
        }
    }

    def parse(self, response):

        for result in response.xpath('//*[@data-component-type="s-search-result"]'):
            name_xpath = './/*[@class="a-size-medium a-color-base a-text-normal"]/text()'
            product_title = result.xpath(name_xpath).get()
            price_dollar = result.xpath('.//*[@class="a-price-whole"]/text()').get()
            price_cents = result.xpath('.//*[@class="a-price-fraction"]/text()').get()

            item = AmazonItem()
            item['Product'] = product_title
            item['Price_Dollars'] = price_dollar
            item['Price_cents'] = price_cents

            yield item
