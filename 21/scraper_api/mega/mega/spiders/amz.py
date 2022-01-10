import scrapy
import scraper_helper as helper
from scrapy.utils.response import open_in_browser
from scrapy.exceptions import CloseSpider
proxy_info = {
  "proxy": "http://scraperapi:API@proxy-server.scraperapi.com:8001"
}
class AmzSpider(scrapy.Spider):
    name = 'amz'
    urls = [
        'https://www.amazon.com/s?rh=n%3A8849526011&fs=true',
        'https://www.amazon.com/s?rh=n%3A8916179011&fs=true',
        'https://www.amazon.com/s?rh=n%3A7939901011&fs=true',
        'https://www.amazon.com/s?k=Wearable+Tech+Virtual+Reality+Gear&i=electronics&rh=n%3A1477500301',
        'https://www.amazon.com/s?rh=n%3A9060176011&fs=true',
        'https://www.amazon.com/s?k=Body+Mounted+Video+Cameras&i=photo&rh=n%3A10048714011',
        'https://www.amazon.com/s?k=Men%27s+Wrist+Watches&i=fashion-mens-watches&rh=n%3A6358540011',
        'https://www.amazon.com/s?k=Women%27s+Wrist+Watches&i=fashion-womens-watches&rh=n%3A6358544011',
        'https://www.amazon.com/s?k=Men%27s+Wrist+Watches&i=fashion-mens-watches&rh=n%3A6358540011',
        'https://www.amazon.com/s?rh=n%3A6459737011&fs=true',
        'https://www.amazon.com/s?rh=n%3A21489946011&fs=true',
        'https://www.amazon.com/s?rh=n%3A6463520011&fs=true',
        'https://www.amazon.com/s?k=DVD+Players+%26+Recorders&i=electronics&rh=n%3A3213027011',
        'https://www.amazon.com/s?i=electronics&rh=n%3A300334&fs=true'
    ]
    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url, meta=proxy_info)
            
    def parse(self, response):
        for result in response.xpath('//*[@data-component-type="s-search-result"]'):
            total_pages = response.xpath('//*[@class="a-pagination"]/li[last()-1]/text()').get()
            current_page = response.xpath('//*[@aria-current="page"]/text()').get()

            if total_pages and current_page:
                if int(current_page) == 1:
                    self.logger.info(f'PAGE {response.url} HAS {total_pages} PAGES.')
                    for i in range(2, int(total_pages) + 1):
                        url = helper.change_param(response.url, 'page', str(i), create_new=True)
                        url = response.urljoin(url)
                        yield scrapy.Request(url, 
                                              callback=self.parse,
                                              meta=proxy_info,
                                              errback = self.handle_error
                                              )

            item = dict()
            item['product_title'] = result.xpath('.//h2//a/span/text()').get()
            rating = result.xpath('.//*[contains(@aria-label,"out of 5 stars")]/@aria-label').get()
            if rating:
                rating = rating.replace('out of 5 stars', '')
            else:
                self.logger.debug(f'Rating not found for {item["product_title"]} at {response.url}')
            item['rating'] = rating
            item['rating_count'] = result.xpath(
                './/*[contains(@aria-label,"out of 5 stars")]/following-sibling::*/@aria-label').get()
            item['price_dollars'] = result.xpath('.//*[@class="a-price-whole"]/text()').get()
            item['price_cents'] = result.xpath('.//*[@class="a-price-fraction"]/text()').get()
            item['asin'] = result.xpath('./@data-asin').get()
            item['details_link'] = response.urljoin(result.xpath('.//h2//a/@href').get())
            item['found_on'] = response.url

            yield item
    def handle_error(self, failure):
        response = failure.value.response
        if response.status == 429:
            open_in_browser(response) # for debugging 429
        # raise CloseSpider('Banned?') # Comment out for proxies
