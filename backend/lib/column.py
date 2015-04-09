#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Justin<justinli.ljt@gmail.com>
# 2015-04-09

from datetime import date

class Meta(object):
    def __init__(self):
        self._value = None 
        self._type = None
        self._empty = None
        self._default = None

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
        if self._type == int:
            return '%s' % self._value
        elif self._type == str:
            return '"%s"' % self._value
        elif self._type == date:
            return '"%s"' % self._value
        else:
            return '"%s"' % self._value

    def valid(self):
        return True

class ColumnInt(Meta):
    def __init__(self, value, emtpy=False, default=0):
        super(ColumnInt, self).__init__()
        self._value = value
        self._type = int
        self._empty = emtpy
        self._default = default

class ColumnStr(Meta):
    def __init__(self, value, emtpy=False, default=0):
        super(ColumnStr, self).__init__()
        self._value = value
        self._type = str
        self._empty = emtpy
        self._default = default

class ColumnDate(Meta):
    def __init__(self, value, emtpy=False, default=0):
        super(ColumnStr, self).__init__()
        self._value = value
        self._type = date
        self._empty = emtpy
        self._default = default

    def cast(self):
        return self._value

class Id(ColumnInt):
    def __init__(self, value):
        super(Id, self).__init__(value, emtpy=False)

if __name__ == '__main__':
    iidd = Id(1001)
    print iidd







