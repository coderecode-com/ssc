import scrapy


class PageLoopSpider(scrapy.Spider):
    name = 'page_loop'
    allowed_domains = ['books.toscrape.com']
    # start_urls = ['https://books.toscrape.com/']
    
    url ='https://books.toscrape.com/catalogue/page-{}.html'
    
    def start_requests(self):
        for i in range(1,51):
            yield scrapy.Request(self.url.format(i))

    def parse(self, response):
        for s in response.xpath('//ol[@class="row"]/li'):
            title = s.xpath('.//img/@alt').get()

            yield {
                'title': title
            }
       