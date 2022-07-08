# Scrapy settings for seleniumDemo project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'seleniumDemo'

SPIDER_MODULES = ['seleniumDemo.spiders']
NEWSPIDER_MODULE = 'seleniumDemo.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'seleniumDemo (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'seleniumDemo.middlewares.SeleniumdemoSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'seleniumDemo.middlewares.SeleniumMiddleware': 543,
   'seleniumDemo.downloadermiddlewares.SeleniumMiddleware': 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'seleniumDemo.pipelines.SeleniumdemoPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


# scrapy配合selenium的配置
import logging

# selenium logging level
GERAPY_SELENIUM_LOGGING_LEVEL = logging.WARNING

# selenium timeout
GERAPY_SELENIUM_DOWNLOAD_TIMEOUT = 30

# selenium browser window
GERAPY_SELENIUM_WINDOW_WIDTH = 1400
GERAPY_SELENIUM_WINDOW_HEIGHT = 700

# selenium settings
GERAPY_SELENIUM_HEADLESS = False
GERAPY_SELENIUM_EXECUTABLE_PATH = None
GERAPY_SELENIUM_IGNORE_HTTPS_ERRORS = False
GERAPY_SELENIUM_PRETEND = True

# selenium args
GERAPY_SELENIUM_DISABLE_EXTENSIONS = True
GERAPY_SELENIUM_HIDE_SCROLLBARS = True
GERAPY_SELENIUM_MUTE_AUDIO = True
GERAPY_SELENIUM_NO_SANDBOX = True
GERAPY_SELENIUM_DISABLE_SETUID_SANDBOX = True
GERAPY_SELENIUM_DISABLE_GPU = True

GERAPY_SELENIUM_SCREENSHOT = None
GERAPY_SELENIUM_SLEEP = 0