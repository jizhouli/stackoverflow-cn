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

from pylogger.pylogger import logger

# add self-defined lib
sys.path.append("../")
from lib.badges_column import *

from store import Store
import config

class Badges(Store):
    '''
    parse dump data from stackoverflow
    '''
    def __init__(self):
        super(Badges, self).__init__()
        self.data = {
                'table': 'badges',
                'column_types': [
                    Id,
                    UserId,
                    Name,
                    Date,
                ],
                }

        logger.info('%s: table %s, column "%s"' % (
            sys._getframe().f_code.co_name, 
            self.data['table'], 
            ','.join(map(lambda x: x.__name__, self.data['column_types']))
            ))

if __name__ == '__main__':
    store = Badges()
    # config db
    _db = config.DEVELOP_DB
    store.conf_db(
            host = _db['host'],
            port = _db['port'],
            user = _db['user'],
            password = _db['password'],
            db = _db['db'],
            )
    # config batch size
    store.conf_batch(config.INSERT_BATCH_SIZE)
    xml_file = '../data/Badges.xml'
    if len(sys.argv) >= 2:
        # python badges.py ~/Downloads/stackoverflow-data-dump-from-MEGA/stackoverflow.com.7z/Badges.xml
        xml_file = sys.argv[1]
    if len(sys.argv) >= 4:
        # python badges.py ~/Downloads/stackoverflow-data-dump-from-MEGA/stackoverflow.com.7z/Badges.xml 1000001 2000000
        start = int(sys.argv[2])
        end = int(sys.argv[3])
    store.load(xml_file, start=start, end=end)

