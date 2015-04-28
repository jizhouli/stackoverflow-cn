#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Justin<justinli.ljt@gmail.com>
# 2015-04-14
'''
STACKOVERFLOW DUMP DATA STORE CLASS

stackoverflow dump data file format specification
http://meta.stackexchange.com/questions/2677/database-schema-documentation-for-the-public-data-dump-and-sede
'''

import os
import sys
import time

#import lxml.etree as ET
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

from pylogger.pylogger import logger

# add self-defined lib
sys.path.append("../")
from lib.umysql import Mysql

class Store(object):
    def __init__(self):
        self.total = 0
        self.data = {
                'table': '',
                'column_types': []
                }
        self.batch_size = 5000

    def __str__(self):
        pass

    def conf_batch(self, batch_size):
        self.batch_size = batch_size
        logger.info('%s: size %s' % (sys._getframe().f_code.co_name, self.batch_size))
        
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

    def load(self, file_path, start=0, end=sys.maxint):
        insert_value_batch = []
        # load file incrementally
        logger.info('%s: file "%s" is loading, row range [%s, %s]' % (sys._getframe().f_code.co_name, file_path, start, end))
        cur_iter = 0
        context = ET.iterparse(file_path, events=('end', )) # ignore event 'start'
        for event, elem in context:
            if elem.tag == 'row': # skip tag <posts>, </posts>
                cur_iter += 1
                if cur_iter > end: # 到达插入范围终点
                    break

                do_continue = False
                if cur_iter < start:
                    do_continue = True # continue

                # wrap column definition to column.py
                #rec['Id'] = elem.attrib.get('Id', 'n/a')
                #rec['PostTypeId'] = elem.attrib.get('PostTypeId', 'n/a')
                #rec['AcceptedAnswerId'] = elem.attrib.get('AcceptedAnswerId', '')
                #print event, elem, elem.attrib.get('Id', 'n/a'), elem.attrib.get('Title', 'answer')

                # 过滤空数据行（预防异常事件）
                if not elem.attrib.get('Id', ''):
                    do_continue = True # continue

                if not do_continue:
                    insert_value = []
                    rec_list = list()
                    for column_type in self.data['column_types']:
                        column = column_type(elem.attrib.get(column_type.__name__, ''))
                        insert_value.append(column.sql())
                    insert_value_batch.append(insert_value)

                    # 批量执行插入操作
                    if len(insert_value_batch) % self.batch_size == 0 and len(insert_value_batch) > 0:
                        logger.info('%s: batch insert row %s %s' % (sys._getframe().f_code.co_name, 
                            cur_iter-len(insert_value_batch)+1, cur_iter))
                        #time.sleep(1)
                        self.exec_insert(self.data['table'], self.data['column_types'], insert_value_batch)
                        insert_value_batch = []

            # 每次循环保证会执行到此处，进行资源释放
            # It's safe to call clear() here because no descendants will be accessed
            elem.clear()
            # Also eliminate now-empty references from the root node to row (USED ONLY in lxml)
            #while elem.getprevious() is not None:
            #    del elem.getparent()[0]

            # end for-loop
        del context
        # 插入剩余数据
        if len(insert_value_batch) > 0:
            logger.info('%s: batch insert row %s %s' % (sys._getframe().f_code.co_name, 
                    cur_iter-len(insert_value_batch)+1, cur_iter))
            self.exec_insert(self.data['table'], self.data['column_types'], insert_value_batch)
            insert_value_batch = []
        logger.info('%s: file load done' % (sys._getframe().f_code.co_name))
        return
