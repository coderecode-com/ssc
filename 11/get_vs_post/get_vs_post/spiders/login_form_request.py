import scrapy
import json
from scrapy import FormRequest


class PostRequestSpider(scrapy.Spider):
    name = 'login_form_request'

    start_urls = ['https://quotes.toscrape.com/login']

    def parse(self, response):
        open_in_browser()
        self.logger.info('Logging In.')
        token = response.xpath('//input[@name="csrf_token"]/@value').get()
        url = 'https://quotes.toscrape.com/login'
        data = {
            'csrf_token': token,
            'username': 'upendra',
            'password': 'secret'
        }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        yield FormRequest(url, formdata=data, headers=headers,
                          callback=self.after_login)

    def after_login(self, response):
        # check login succeed before going on
        logout_link = response.xpath('//a[text()="Logout"]/@href').get()
        if not logout_link:
            self.logger.error("Login failed")
            return
        self.logger.info("Logged in.")
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

        yield response.follow(logout_link,
                              callback=self.after_logout,
                              dont_filter=True)

    def after_logout(self, response):
        login_link = response.xpath('//a[text()="Login"]/@href').get()
        if login_link:
            self.logger.info('Logged out')
        else:
            self.logger.error('Logout failed')
