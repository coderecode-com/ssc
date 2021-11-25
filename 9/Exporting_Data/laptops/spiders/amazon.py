import scrapy


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.com']

    # start_urls = ['https://www.amazon.com/s?k=laptop']

    def start_requests(self):
        yield scrapy.Request(url="https://www.amazon.com/s?k=laptop")

    def parse(self, response):
        for result in response.xpath('//*[@data-component-type="s-search-result"]'):
            name_xpath = './/*[@class="a-size-medium a-color-base a-text-normal"]/text()'
            product_title = result.xpath(name_xpath).get()
            price_dollar = result.xpath('.//*[@class="a-price-whole"]/text()').get()
            price_cents = result.xpath('.//*[@class="a-price-fraction"]/text()').get()

            item = dict()
            item['Product'] = product_title
            item['Price_Dollars'] = price_dollar
            item['Price_cents'] = price_cents

            yield item
