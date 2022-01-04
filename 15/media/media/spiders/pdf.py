import scrapy
from media.items import MediaItem

class PdfSpider(scrapy.Spider):
    name = 'pdf'
    start_urls = ['https://www.scrapebay.com/ebooks']

    def parse(self, response):
        for s in response.xpath('//*[@class="col"]'):
            pdf_link = response.urljoin(s.xpath('.//*[contains(@class,"pdf")]/@href').get())
            image_link = response.urljoin(s.xpath('.//*[@class="card-img-top"]/@src').get())
            item = MediaItem()

            item['BookTitle'] = s.xpath('.//*[@class="card-title"]/text()').get()
            item['file_urls'] = [pdf_link]
            item['image_urls'] = [image_link]
            
            yield item
