# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import sys
import hashlib

from scrapy import log
from scrapy.exceptions import DropItem

# add self-defined lib
sys.path.append("../../")
from lib.umysql import Mysql

class MD5SumPipeline(object):
    def process_item(self, item, spider):
        plain_txt = '%s+%s' % ('justin', item['name'])
        m = hashlib.md5()
        m.update(plain_txt)
        md5 = m.hexdigest()
        log.msg("\"%s\" md5sum %s" % (plain_txt, md5))

        item['md5'] = md5
        return item

class ValidatePipeline(object):
    def process_item(self, item, spider):
        return item

class StoreToDBPipeline(object):
    def process_item(self, item, spider):
        return item

