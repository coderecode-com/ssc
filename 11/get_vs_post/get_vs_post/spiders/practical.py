import scrapy
from scrapy import FormRequest


class AspxSpider(scrapy.Spider):
    name = 'aspx'
    start_urls = ['https://www.unspsc.org/search-code']

    def parse(self, response, **kwargs):
        form = {
            'dnn$ctr1535$UNSPSCSearch$txtsearchCode': '',
            'dnn$ctr1535$UNSPSCSearch$txtSearchTitle': 'organic',
            'dnn$ctr1535$UNSPSCSearch$btnSearch': 'Search',
        }

        yield FormRequest.from_response(response,
                                        formdata=form,
                                        callback=self.parse_table)

    def parse_table(self, response):
        rows = response.xpath('//table[contains(@id, "gvDetailsSearchView")]//tr[td]')
        for row in rows:
            if row.xpath('./td[1]/text()').get():
                yield {
                    'code': row.xpath('./td[1]/text()').get(),
                    'value': row.xpath('./td[2]/text()').get()
                }
