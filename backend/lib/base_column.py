#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Justin<justinli.ljt@gmail.com>
# 2015-04-09

from datetime import date

'''
EXCHANGEOVERFLOW DATA DUMP MODEL
reference to:
   http://meta.stackexchange.com/questions/2677/database-schema-documentation-for-the-public-data-dump-and-sede
   https://gist.github.com/gousiosg/7600626
'''

#### basic class for all column type ####

class Meta(object):
    def __init__(self, value, type, empty):
        self._value = value
        self._type = type
        self._empty = empty

    def __str__(self):
        s = ''
        s += '%s\n' % self._value
        s += 'type:\t%s\n' % self._type
        s += 'name:\t%s\n' % self.name()
        s += 'empty:\t%s\n' % self.empty()
        s += 'cast:\t%s (%s)\n' % (self.cast(), type(self.cast()))
        s += 'sql:\t%s (%s)\n' % (self.sql(), type(self.cast()))
        s += 'valid:\t%s' % self.valid()
        return s

    def name(self):
        return self.__class__.__name__

    def empty(self):
        return self._empty

    def cast(self):
        return self._type(self._value)

    def sql(self):
        # process null
        if self._value == None:
            return '""'

        if self._type == int:
            if self._value:
                return '%s' % self._value
            else:
                return '0' # to insert null int, default 0
        elif self._type == str:
            s = self._value
            s = s.replace('\\', '\\\\') # deal with situation [ \" ]
            s = s.replace('"', '\\"')
            s = '"%s"' % s
            return s
            #return '"%s"' % self._value.replace('"', '\\"') # escape double quotes to avoid sql string's
        elif self._type == date:
            if self._value:
                return '"%s"' % self._value
            else:
                return '"1971-01-01 00:00:00.000"'
        else:
            return '"%s"' % self._value

    def valid(self):
        return True

    def comment(self):
        return ''

#### data type for all column type ####

class ColumnInt(Meta):
    def __init__(self, value, empty=True):
        super(ColumnInt, self).__init__(value, type=int, empty=empty)

class ColumnStr(Meta):
    def __init__(self, value, empty=True):
        super(ColumnStr, self).__init__(value, type=str, empty=empty)

class ColumnDate(Meta):
    def __init__(self, value, empty=True):
        super(ColumnDate, self).__init__(value, type=date, empty=empty)

    def cast(self):
        return self._value

