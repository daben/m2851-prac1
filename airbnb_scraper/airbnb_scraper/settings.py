# -*- coding: utf-8 -*-

# Scrapy settings for airbnb_scraper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'airbnb_scraper'

SPIDER_MODULES = ['airbnb_scraper.spiders']
NEWSPIDER_MODULE = 'airbnb_scraper.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = f'{BOT_NAME} (+http://www.uoc.edu)'
# USER_AGENT = ("Mozilla/5.0 (iPhone; CPU iPhone OS 8_0_2 like Mac OS X)"
#               " AppleWebKit/600.1.4 (KHTML, like Gecko) "
#               " Version/8.0 Mobile/12A366 Safari/600.1.4")

# Public development key
AIRBNB_API_KEY = 'd306zoyjsyarp7ifhu67rjxn52tv0t20'

# FEED_EXPORT_FIELDS = 'id,name,user_id,user_name,neighborhood,city,section_offset'.split(',')

# Obey robots.txt rules
ROBOTSTXT_OBEY = True
WEB_BROWSER = 'chromium'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 5
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'airbnb_scraper.middlewares.AirbnbScraperSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    # 'airbnb_scraper.middlewares.AirbnbScraperDownloaderMiddleware': 543,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'airbnb_scraper.pipelines.DuplicatesPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html

# It uses download latency to compute the delays. The main idea is
# the following: if a server needs latency seconds to respond,
# a client should send a request each latency/N seconds to have
# N requests processed in parallel.

AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 10
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = [503]
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
