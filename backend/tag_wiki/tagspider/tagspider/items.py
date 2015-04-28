# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TagspiderItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    sum = scrapy.Field()
    excerpt = scrapy.Field()
    wiki = scrapy.Field()

    md5 = scrapy.Field()

