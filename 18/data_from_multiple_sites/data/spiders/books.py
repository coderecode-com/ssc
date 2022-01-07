import scrapy


class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com',
                       'www.gutenberg.org']
    start_urls = ['https://books.toscrape.com/']

    def parse(self, response):
        for s in response.xpath('//article'):
            item = {}
            item['price'] = s.xpath('.//p[@class="price_color"]/text()').get()
            link = response.urljoin(s.xpath('.//h3/a/@href').get())

            yield scrapy.Request(link,
                                 cb_kwargs={
                                     'item': item
                                 },
                                 callback=self.parse_book_details)

    def parse_book_details(self, response, item):
        item['Title'] = response.xpath('//article//h1/text()').get()
        item['UPC'] = response.xpath('//*[text()="UPC"]/following-sibling::*/text()').get()
        url = 'https://www.gutenberg.org/ebooks/search/?query={}&submit_search=Go%21'
        yield scrapy.Request(url.format(item['Title']),
                             cb_kwargs={
                                 'item': item
                             },
                             callback=self.parse_gutenberg)

    def parse_gutenberg(self, response, item):
        number_of_matches = len(response.xpath('//li[@class="booklink"]').getall())
        item['Gutenberg_Matches'] = number_of_matches
        yield item


from scraper_helper import run_spider