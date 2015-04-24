# -*- coding: utf-8 -*-

# Scrapy settings for tagspider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:16.0) Gecko/20100101 Firefox'
BOT_VERSION = '1.0'

CONCURRENT_REQUESTS = 2

SPIDER_MODULES = ['tagspider.spiders']
NEWSPIDER_MODULE = 'tagspider.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tagspider (+http://www.yourdomain.com)'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

ITEM_PIPELINES = [
        ]
