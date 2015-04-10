#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Justin<justinli.ljt@gmail.com>
# 2015-04-08
'''
STACKOVERFLOW DUMP DATA STORE CLASS

stackoverflow dump data file format specification
http://meta.stackexchange.com/questions/2677/database-schema-documentation-for-the-public-data-dump-and-sede
'''

import os
import sys
import time

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

from pylogger.pylogger import logger

# add self-defined lib
sys.path.append("../")
from lib.umysql import Mysql
from lib.column import *

import config

class DumpParse(object):
    '''
    parse dump data from stackoverflow
    '''
    def __init__(self):

        #self.post_column_types = [Id, PostTypeId, AcceptedAnswerId, ParentID, CreationDate, Score, ViewCount, Body, OwnerUserId, OwnerDisplayName, LastEditorUserId, LastEditorDisplayName, LastEditDate, LastActivityDate, Title, Tags, AnswerCount, CommentCount, FavoriteCount, ClosedDate, CommunityOwnedDate]
        self.posts = {
                'table': 'Posts',
                'column_types': [
                    Id,
                    PostTypeId,
                    AcceptedAnswerId,
                    ParentID,
                    Score,
                    ViewCount,
                    Body,
                    OwnerUserId,
                    LastEditorUserId,
                    LastEditDate,
                    LastActivityDate,
                    Title,
                    Tags,
                    AnswerCount,
                    CommentCount,
                    FavoriteCount,
                    CreationDate,
                ],
                }
        pass

    def __str__(self):
        pass

    def conf_db(self, user, password, host, db, port=3306):
        self.user = user
        self.password = password
        self.host = host
        self.db = db
        self.port = port

        self.conn = Mysql(host=self.host, user=self.user, password=self.password, db=self.db, port=self.port)
        #self.conn.show()
        pass

    def exec_insert(self, table, cols, insert_value_batch):
        # 判断column与value数目是否相等
        if len(insert_value_batch) == 0:
            print 'insert_value_batch is emtpy'
            print insert_value_batch
            return False
        if len(insert_value_batch[0]) != len(cols):
            print 'SIZE cols %s, insert_value_batch %s' % (len(cols),  len(insert_value_batch[0]))
            print cols
            print  len(insert_value_batch[0])
            return False

        vals = []
        for insert_value in insert_value_batch:
            val = '(%s)' % (','.join(insert_value))
            vals.append(val)
        vals = ','.join(vals)

        sql = 'INSERT INTO %(table)s (%(cols)s) VALUES %(vals)s;'
        para = {
                'table': table,
                'cols': ','.join(map(lambda x: x.__name__, cols)),
                'vals': vals,
            }
        sql %= para
        self.conn.execute(sql)
        pass

    def load_posts(self, file_path):
        insert_value_batch = []
        cnt = 0
        # load file incrementally
        for event, elem in ET.iterparse(file_path, events=('end', )): # ignore event 'start'
            if elem.tag == 'row': # skip tag <posts>, </posts>
                # wrap column definition to column.py
                #rec['Id'] = elem.attrib.get('Id', 'n/a')
                #rec['PostTypeId'] = elem.attrib.get('PostTypeId', 'n/a')
                #rec['AcceptedAnswerId'] = elem.attrib.get('AcceptedAnswerId', '')
                #print event, elem, elem.attrib.get('Id', 'n/a'), elem.attrib.get('Title', 'answer')

                # 过滤空数据行（预防异常事件）
                if not elem.attrib.get('Id', ''):
                    continue

                insert_value = []
                rec_list = list()
                for column_type in self.posts['column_types']:
                    column = column_type(elem.attrib.get(column_type.__name__, ''))
                    insert_value.append(column.sql())
                insert_value_batch.append(insert_value)
            elem.clear()
            # 批量执行插入操作
            if len(insert_value_batch) % config.INSERT_BATCH_SIZE == 0 and len(insert_value_batch) > 0:
                print cnt
                time.sleep(1)
                self.exec_insert(self.posts['table'], self.posts['column_types'], insert_value_batch)
                insert_value_batch = []
                #TODO
                break
            cnt += 1
        # 插入剩余数据
        if len(insert_value_batch) > 0:
            self.exec_insert(self.posts['table'], self.posts['column_types'], insert_value_batch)
            insert_value_batch = []
        return

    def load_post_history(self, file_path):
        pass
    def load_comments(self, file_path):
        pass
    def load_votes(self, file_path):
        pass
    def load_badges(self, file_path):
        pass
    def load_users(self, file_path):
        pass
    pass

if __name__ == '__main__':
    dp = DumpParse()
    dp.conf_db(
            host = config.ONLINE_DB['host'],
            port = config.ONLINE_DB['port'],
            user = config.ONLINE_DB['user'],
            password = config.ONLINE_DB['password'],
            db = config.ONLINE_DB['db'],
            )
    dp.load_posts('../data/Posts.xml')

