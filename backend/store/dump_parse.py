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

        self.colums = [Id, PostTypeId, AcceptedAnswerId, ParentID, CreationDate, Score, ViewCount, Body, OwnerUserId, OwnerDisplayName, LastEditorUserId, LastEditorDisplayName, LastEditDate, LastActivityDate, Title, Tags, AnswerCount, CommentCount, FavoriteCount, ClosedDate, CommunityOwnedDate]
        pass

    def __str__(self):
        pass

    def conf_db(self, user, password, host, db, port=3306):
        self.user = user
        self.password = password
        self.host = host
        self.db = db
        self.port = port

        #self.conn =  Mysql(host=self.host, user=self.user, password=self.password, db=self.db, port=self.port)
        #self.conn.show()
        pass

    def patch_store(self, title_list, record_list, batch_size=10000):
        pass

    def load_posts_incr(self, file_path):
        print self.colums
        return
        cnt = 1
        batch_records = []
        for event, elem in ET.iterparse(file_path, events=('start', 'end', 'start-ns', 'end-ns')):
            if elem.tag == 'row': # skip tag <posts>
                rec = dict()
                rec['Id'] = elem.attrib.get('Id', 'n/a')
                rec['PostTypeId'] = elem.attrib.get('PostTypeId', 'n/a')
                rec['AcceptedAnswerId'] = elem.attrib.get('AcceptedAnswerId', '')
                print event, elem, elem.attrib.get('Id', 'n/a'), elem.attrib.get('Title', 'answer')
            elem.clear()
            cnt += 1
            if cnt%100000 == 0:
                time.sleep(1)
        return

    def load_posts(self, file_path):
        tree = ET.ElementTree(file=file_path)
        root = tree.getroot()
        #print root.tag, root.attrib
        cnt = 1
        for row in root:
            #print row.tag, row.attrib
            if row.tag == 'row':
                print 'Id', row.attrib['Id']
                print 'PostTypeId', row.attrib['PostTypeId']
                print 'Title', row.attrib.get('Title', 'n/a')
                print 'Body', len(row.attrib['Body'])
                print 'AcceptedAnswerId', row.attrib.get('AcceptedAnswerId', 'n/a')
                print 'ParentId', row.attrib.get('ParentId', 'n/a')
            cnt += 1
            if cnt > 1000:
                break

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
    dp.load_posts_incr('../data/Posts.xml')

