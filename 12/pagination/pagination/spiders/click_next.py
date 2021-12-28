import scrapy


class ClickNextSpider(scrapy.Spider):
    name = 'click_next'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/']

    def parse(self, response):
        for s in response.xpath('//ol[@class="row"]/li'):
            title = s.xpath('.//img/@alt').get()

            yield {
                'title': title
            }
        next_page = response.xpath('//a[@class="next"]/@href').get()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page))
