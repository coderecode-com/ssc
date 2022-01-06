import scrapy


class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/']

    def parse(self, response):
        for s in response.xpath('//article')[:2]:
            item = {}
            item['price'] = s.xpath('.//p[@class="price_color"]/text()').get()
            item['link'] = response.urljoin(s.xpath('.//h3/a/@href').get())
            footer_text = response.xpath('//*[@class="current"]/text()').get()
            yield scrapy.Request(item['link'],
                                 cb_kwargs={
                                     'item': item,
                                     'footer': footer_text
            },
                callback=self.parse_book_details)

    def parse_book_details(self, response, item,footer):
        # print(item)
        # print(footer)
        item['UPC'] = response.xpath('//*[text()="UPC"]/following-sibling::*/text()').get()
        yield item
