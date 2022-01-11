import scraper_helper as helper
import scrapy


class SchoolsSpider(scrapy.Spider):
    name = "schools"
    start_urls = ["https://directory.ntschools.net/#/schools"]

    def parse(self, response):
        headers = helper.get_dict(
            '''
            Accept: application/json
            Accept-Encoding: gzip, deflate, br
            Accept-Language: en-GB,en;q=0.9
            Connection: keep-alive
            Host: directory.ntschools.net
            Referer: https://directory.ntschools.net/
            Sec-Fetch-Dest: empty
            Sec-Fetch-Mode: cors
            Sec-Fetch-Site: same-origin
            Sec-GPC: 1
            User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36
            X-Requested-With: Fetch
                        '''
        )
        yield scrapy.Request(
            url="https://directory.ntschools.net/api/System/GetAllSchools",
            callback=self.parse_json,
            headers=headers,
        )

    def parse_json(self, response):
        headers = helper.get_dict('''
            Accept: application/json
            Accept-Encoding: gzip, deflate, br
            Accept-Language: en-GB,en;q=0.9
            Connection: keep-alive
            Host: directory.ntschools.net
            Referer: https://directory.ntschools.net/
            Sec-Fetch-Dest: empty
            Sec-Fetch-Mode: cors
            Sec-Fetch-Site: same-origin
            Sec-GPC: 1
            User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36
            X-Requested-With: Fetch
            ''')
        data = response.json()

        for school in data:
            school_code = school["itSchoolCode"]
            yield scrapy.Request(
                f"https://directory.ntschools.net/api/System/GetSchool?itSchoolCode={school_code}",
                callback=self.parse_school,
                headers=headers,
            )

    def parse_school(self, response):
        data = response.json()

        yield {
            "name": data["name"],
            "telephoneNumber": data["telephoneNumber"],
            "mail": data["mail"],
            "physicalAddress": data["physicalAddress"]["displayAddress"],
            "postalAddress": data["postalAddress"]["displayAddress"],
        }
