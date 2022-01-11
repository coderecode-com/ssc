import scraper_helper

from rotating.spiders.proxy import ProxySpider

if __name__ == '__main__':
    scraper_helper.run_spider(ProxySpider)
