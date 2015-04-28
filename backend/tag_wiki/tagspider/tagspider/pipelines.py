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
from config import DEVELOP_DB, ONLINE_DB

class MD5SumPipeline(object):
    def process_item(self, item, spider):
        plain_txt = '%s+%s' % ('justin', item['name'])
        m = hashlib.md5()
        m.update(plain_txt)
        md5 = m.hexdigest()
        log.msg("\"%s\" md5sum %s" % (plain_txt, md5))

        item['md5'] = md5
        return item

class SQLStatementEscape(object):
    def process_item(self, item, spider):
        item['excerpt'] = self.sql_escape(item['excerpt'])
        item['wiki'] = self.sql_escape(item['wiki'])
        return item

    def sql_escape(self, string):
        string = string.replace('\\', '\\\\') # deal with situation [ \" ]
        string = string.replace('"', '\\"')
        return string

class ValidatePipeline(object):
    def process_item(self, item, spider):
        return item

class StoreToDBPipeline(object):
    def __init__(self):
        self.host = ONLINE_DB['host']
        self.user = ONLINE_DB['user']
        self.password = ONLINE_DB['password']
        self.db = ONLINE_DB['db']
        self.port = ONLINE_DB['port']

        self.conn = None
        self.retry_times = 3
        log.msg("-"*1000)
        self.connect()
        log.msg("-"*1000)
        self.insert_sql = 'INSERT INTO meta_tag (Name, Sum, Excerpt, Wiki, MD5) VALUES("%s", %s, "%s", "%s", "%s");'
        pass

    def connect(self):
        for retry in range(self.retry_times):
            try:
                if self.conn:
                    self.conn.close()
                self.conn = Mysql(host=self.host, user=self.user, password=self.password, db=self.db, port=self.port)
                break
            except Exception, e:
                log.msg(str(e), level=log.ERROR)
                self.conn = None
            log.msg('connect db retry %s times' % (retry+1), level=log.WARNING)
        # end-for

    def process_item(self, item, spider):
        sql = self.insert_sql % (item['name'], item['sum'], item['excerpt'], item['wiki'], item['md5'])
        log.msg(sql)
        
        for retry in range(self.retry_times):
            try:
                self.conn.execute(sql)
                break
            except Exception, e:
                log.msg(str(e), level=log.ERROR)
                # 处理连接丢失的情况
                # (2013, 'Lost connection to MySQL server during query')
                # (2006, 'MySQL server has gone away')
                if True:# e.errno == 2013 or e.errno == 2006:
                    self.connect()
                else:
                    log.msg("tag %s store failed" % item['name'], level=log.ERROR)
                    break
        
        return item

