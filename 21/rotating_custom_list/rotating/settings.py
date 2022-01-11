BOT_NAME = 'rotating'

SPIDER_MODULES = ['rotating.spiders']
NEWSPIDER_MODULE = 'rotating.spiders'

ROBOTSTXT_OBEY = False
ROTATING_PROXY_LIST_PATH = 'proxy_list.txt'
DOWNLOADER_MIDDLEWARES = {
    'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
    'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
}
