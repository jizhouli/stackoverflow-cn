#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Justin<justinli.ljt@gmail.com>
# 2015-04-09

from base_column import *

#### column type - Comments ####

class Id(ColumnInt):
    def __init__(self, value):
        super(Id, self).__init__(value, empty=False)

class PostId(ColumnInt):
    def __init__(self, value):
        super(PostId, self).__init__(value, empty=False)

class Score(ColumnInt):
    def __init__(self, value):
        super(Score, self).__init__(value)

    def comment(self):
        s = '''only present if score > 0'''
        return s

class Text(ColumnStr):
    def __init__(self, value):
        super(Text, self).__init__(value)

    def comment(self):
        s = '''@Stu Thompson: What a horrible idea, you clueless git!'''
        return s

class CreationDate(ColumnDate):
    def __init__(self, value):
        super(CreationDate, self).__init__(value)

class UserDisplayName(ColumnStr):
    def __init__(self, value):
        super(UserDisplayName, self).__init__(value)

class UserId(ColumnInt):
    def __init__(self, value):
        super(UserId, self).__init__(value, empty=False)

    def comment(self):
        s = '''optional. Absent if user has been deleted?'''
        return s

if __name__ == '__main__':
    iidd = Id(1001)
    print iidd

    pi = PostId(1222)
    print pi

    score = Score(100)
    print score
    print score.comment()

    text = Text('@john: Thank you!')
    print text
    print text.comment()

    cd = CreationDate('2009-03-05T22:28:34.823')
    print cd

    udn = UserDisplayName('Johnney')
    print udn

    uid = UserId(1001)
    print uid
    print uid.comment()

