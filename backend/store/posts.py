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
from lib.posts_column import *

import config

class Posts(object):
    '''
    parse dump data from stackoverflow
    '''
    def __init__(self):

        self.total = 0
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

        logger.info('%s: table %s, column "%s"' % (
            sys._getframe().f_code.co_name, 
            self.posts['table'], 
            ','.join(map(lambda x: x.__name__, self.posts['column_types']))
            ))

    def __str__(self):
        pass

    def conf_db(self, user, password, host, db, port=3306):
        self.user = user
        self.password = password
        self.host = host
        self.db = db
        self.port = port

        self.conn = Mysql(host=self.host, user=self.user, password=self.password, db=self.db, port=self.port)
        logger.info('%s: %s@%s:%s %s' % (sys._getframe().f_code.co_name, self.user, self.host, self.port, self.db))

    def exec_insert(self, table, cols, insert_value_batch):
        # 判断column与value数目是否相等
        if len(insert_value_batch) == 0:
            logger.warn('%s: insert value batch is empty' % (sys._getframe().f_code.co_name))
            return False
        if len(insert_value_batch[0]) != len(cols):
            logger.warn('%s: column size is not equal to value, col %s val %s' % (sys._getframe().f_code.co_name, len(cols), len(insert_value_batch[0])))
            return False

        vals = []
        for insert_value in insert_value_batch:
            val = '(%s)' % (','.join(insert_value))
            vals.append(val)
        vals = ','.join(vals)

        sql = 'INSERT IGNORE INTO %(table)s (%(cols)s) VALUES %(vals)s;'
        para = {
                'table': table,
                'cols': ','.join(map(lambda x: x.__name__, cols)),
                'vals': vals,
            }
        sql %= para
        while True:
            try:
                self.conn.execute(sql)
                break
            except Exception, e:
                logger.error(str(e))
                # 处理连接丢失的情况
                # (2013, 'Lost connection to MySQL server during query')
                # (2006, 'MySQL server has gone away')
                if e.errno == 2013 or e.errno == 2006:
                    self.conn.close()
                    self.conn = Mysql(host=self.host, user=self.user, password=self.password, db=self.db, port=self.port)
                    logger.warn('%s: reconnect %s@%s:%s %s' % (sys._getframe().f_code.co_name, self.user, self.host, self.port, self.db))
                else:
                    return False

        self.total += len(insert_value_batch)
        logger.info('%s: insert %s/%s' % (sys._getframe().f_code.co_name, len(insert_value_batch), self.total))
        return True

    def load_posts(self, file_path, start=0, end=sys.maxint):
        insert_value_batch = []
        # load file incrementally
        logger.info('%s: file "%s" is loading, row range [%s, %s]' % (sys._getframe().f_code.co_name, file_path, start, end))
        cur_iter = 0
        for event, elem in ET.iterparse(file_path, events=('end', )): # ignore event 'start'
            if elem.tag == 'row': # skip tag <posts>, </posts>
                cur_iter += 1
                if cur_iter < start:
                    continue
                if cur_iter > end:
                    break
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
                logger.info('%s: batch insert row %s %s' % (sys._getframe().f_code.co_name, 
                    cur_iter-len(insert_value_batch)+1, cur_iter))
                #time.sleep(1)
                self.exec_insert(self.posts['table'], self.posts['column_types'], insert_value_batch)
                insert_value_batch = []
        # 插入剩余数据
        if len(insert_value_batch) > 0:
            logger.info('%s: batch insert row %s %s' % (sys._getframe().f_code.co_name, 
                    cur_iter-len(insert_value_batch)+1, cur_iter))
            self.exec_insert(self.posts['table'], self.posts['column_types'], insert_value_batch)
            insert_value_batch = []
        logger.info('%s: file load done' % (sys._getframe().f_code.co_name))
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
    posts = Posts()
    _db = config.ONLINE_DB
    posts.conf_db(
            host = _db['host'],
            port = _db['port'],
            user = _db['user'],
            password = _db['password'],
            db = _db['db'],
            )
    post_xml_file = '../data/Posts.xml'
    if len(sys.argv) >= 2:
        post_xml_file = sys.argv[1]
    if len(sys.argv) >= 4:
        start = int(sys.argv[2])
        end = int(sys.argv[3])
    posts.load_posts(post_xml_file, start=start, end=end)

