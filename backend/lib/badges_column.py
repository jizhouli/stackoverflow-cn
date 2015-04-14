#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Justin<justinli.ljt@gmail.com>
# 2015-04-09

from base_column import *

#### column type - Badges ####

class Id(ColumnInt):
    def __init__(self, value):
        super(Id, self).__init__(value, empty=False)

class UserId(ColumnInt):
    def __init__(self, value):
        super(UserId, self).__init__(value, empty=False)

class Name(ColumnStr):
    def __init__(self, value):
        super(Name, self).__init__(value)

    def comment(self):
        s = '''e.g.: "Teacher"'''
        return s

class Date(ColumnDate):
    def __init__(self, value):
        super(Date, self).__init__(value)

if __name__ == '__main__':
    iidd = Id(1001)
    print iidd

    ui = UserId(1211)
    print ui

    name = Name('Engineer')
    print name
    print name.comment()

    d = Date('2009-03-05T22:28:34.823')
    print d

