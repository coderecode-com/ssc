import scrapy
import scraper_helper as helper


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.com']

    # start_urls = ['https://www.amazon.com/s?k=laptop']

    def start_requests(self):
        yield scrapy.Request(url="https://www.amazon.com/s?k=laptop")

    def parse(self, response):
        customer_headers = helper.get_dict('''
            Accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8
            Accept-Encoding: gzip, deflate, br
            Accept-Language: en-US,en;q=0.9
            Cache-Control: no-cache
            Connection: keep-alive
            Cookie: session-id=142-7859842-5382350; session-id-time=2082787201l; i18n-prefs=USD; ubid-main=134-0962554-6201357; session-token=kJAt4M26GZtNQIa5muh7oHzQaupI0q1Ue4miw/Q7QYYPJ/Ma60fPPxrX3zKrmTrJGxpJtceEfQYgUEqBe40DRXEKenis5NXZAZ7Kreffi995+xLtcuzZCxPbLCUENbsoAll9889xnVWgHfp41j/ifS0ibRYHprJvvUUJ+Jt/nNOBzWjipiG/QCr2DjGkGt4R
            Host: aax-us-iad.amazon.com
            Pragma: no-cache
            Referer: https://www.amazon.com/
            sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"
            sec-ch-ua-mobile: ?0
            sec-ch-ua-platform: "macOS"
            Sec-Fetch-Dest: image
            Sec-Fetch-Mode: no-cors
            Sec-Fetch-Site: same-site
            User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36
        ''')
        print(customer_headers)
        print(response.xpath('//title/text()').get())
