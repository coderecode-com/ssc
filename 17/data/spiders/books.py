import scrapy


class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/']

    def parse(self, response):
        for s in response.xpath('//article')[:2]:
            item = {}
            item['price'] = s.xpath('.//p[@class="price_color"]/text()').get()
            link = response.urljoin(s.xpath('.//h3/a/@href').get())
            yield scrapy.Request(link,
                                 cb_kwargs={
                                     'item': item
                                 },
                                 callback=self.parse_book_details)

    def parse_book_details(self, response, item):
        item['UPC'] = response.xpath('//*[text()="UPC"]/following-sibling::*/text()').get()
        item['Title'] = response.xpath('//article//h1/text()').get()
        yield item


###
