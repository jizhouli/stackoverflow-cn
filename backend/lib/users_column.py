#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Justin<justinli.ljt@gmail.com>
# 2014-04-14

from base_column import *

#### column type - Users

class Id(ColumnInt):
    def __init__(self, value):
        super(Id, self).__init__(value, empty=False)

class Reputation(ColumnInt):
    def __init__(self, value):
        super(Reputation, self).__init__(value, empty=False)

class CreationDate(ColumnDate):
    def __init__(self, value):
        super(CreationDate, self).__init__(value)

class DisplayName(ColumnStr):
    def __init__(self, value):
        super(DisplayName, self).__init__(value)

class LastAccessDate(ColumnDate):
    def __init__(self, value):
        super(LastAccessDate, self).__init__(value)

class Views(ColumnInt):
    def __init__(self, value):
        super(Views, self).__init__(value)

class WebsiteUrl(ColumnStr):
    def __init__(self, value):
        super(WebsiteUrl, self).__init__(value)

class Location(ColumnStr):
    def __init__(self, value):
        super(Location, self).__init__(value)

class AboutMe(ColumnStr):
    def __init__(self, value):
        super(AboutMe, self).__init__(value)

class Age(ColumnInt):
    def __init__(self, value):
        super(Age, self).__init__(value)

class UpVotes(ColumnInt):
    def __init__(self, value):
        super(UpVotes, self).__init__(value)

class DownVotes(ColumnInt):
    def __init__(self, value):
        super(DownVotes, self).__init__(value)

class EmailHash(ColumnStr):
    def __init__(self, value):
        super(EmailHash, self).__init__(value)

    def comment(self):
        s = '''now always blank'''
        return s

class AccountId(ColumnInt):
    def __init__(self, value):
        super(AccountId, self).__init__(value)

    def comment(self):
        s = '''StackExchange Network profile Id of the user'''
        return s


if __name__ == '__main__':
    iidd = Id(1001)
    print iidd

    reputation = Reputation(99)
    print reputation

    cd = CreationDate('2009-03-05T22:28:34.823')
    print cd

    dn = DisplayName('Jonney')
    print dn

    lad = LastAccessDate('2009-03-05T22:28:34.823')
    print lad

    views = Views(90)
    print views

    wu = WebsiteUrl('http://imuser.com')
    print wu

    l = Location('Queen AVE, NY')
    print l

    am = AboutMe('haha, I am genius')
    print am

    age = Age(23)
    print age

    uv = UpVotes(1421)
    print uv

    dv = DownVotes(211)
    print dv

    eh = EmailHash('d41d8cd98f00b204e9800998ecf8427e')
    print eh
    print eh.comment()

    ai = AccountId(1)
    print ai
    print ai.comment()

