#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Justin<justinli.ljt@gmail.com>
# 2015-04-08

DEVELOP_DB = {
        'host': 'stackexchange.mysql.rds.aliyuncs.com',
        'port': 3306,
        'user': 'himalayas',
        'password': 'himalayas2015',
        'db': 'stackoverflow_dev',
        }

ONLINE_DB = {
        'host': 'stackexchange.mysql.rds.aliyuncs.com',
        'port': 3306,
        'user': 'himalayas',
        'password': 'himalayas2015',
        'db': 'stackoverflow',
        }

INSERT_BATCH_SIZE = 5000
