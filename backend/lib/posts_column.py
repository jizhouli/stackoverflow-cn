#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Justin<justinli.ljt@gmail.com>
# 2015-04-09

from base_column import *

#### column type - Posts ####

class Id(ColumnInt):
    def __init__(self, value):
        super(Id, self).__init__(value, empty=False)

class PostTypeId(ColumnInt):
    def __init__(self, value):
        super(PostTypeId, self).__init__(value, empty=False)

    def comment(self):
        s = '''post type id meaning:
        1. Question
        2. Answer
        3. Orphaned tag wiki
        4. Tag wiki excerpt
        5. Tag wiki
        6. Moderator nomination
        7. "Wiki placeholder"
        8. Privilege wiki'''
        return s

class AcceptedAnswerId(ColumnInt):
    def __init__(self, value):
        super(AcceptedAnswerId, self).__init__(value)

    def comment(self):
        s = '''only present if PostTypeId is 1'''
        return s

class ParentID(ColumnInt):
    def __init__(self, value):
        super(ParentID, self).__init__(value)

    def comment(self):
        s = '''only present if PostTypeId is 2'''
        return s

class CreationDate(ColumnDate):
    def __init__(self, value):
        super(CreationDate, self).__init__(value)

class Score(ColumnInt):
    def __init__(self, value):
        super(Score, self).__init__(value)

class ViewCount(ColumnInt):
    def __init__(self, value):
        super(ViewCount, self).__init__(value)

class Body(ColumnStr):
    def __init__(self, value):
        super(Body, self).__init__(value)

class OwnerUserId(ColumnInt):
    def __init__(self, value):
        super(OwnerUserId, self).__init__(value, empty=False)

    def comment(self):
        s = '''present only if user has not been deleted; always -1 for tag wiki entries (i.e., the community user owns them)'''
        return s

class OwnerDisplayName(ColumnStr):
    def __init__(self, value):
        super(OwnerDisplayName, self).__init__(value)

class LastEditorUserId(ColumnInt):
    def __init__(self, value):
        super(LastEditorUserId, self).__init__(value, empty=False)

class LastEditorDisplayName(ColumnStr):
    def __init__(self, value):
        super(LastEditorDisplayName, self).__init__(value)

class LastEditDate(ColumnDate):
    def __init__(self, value):
        super(LastEditDate, self).__init__(value)

class LastActivityDate(ColumnDate):
    def __init__(self, value):
        super(LastActivityDate, self).__init__(value)

    def comment(self):
        s = '''the date and time of the most recent activity on the post. For a question, this could be the post being edited, a new answer was posted, a bounty was started, etc.'''
        return s

class Title(ColumnStr):
    def __init__(self, value):
        super(Title, self).__init__(value, empty=False)

class Tags(ColumnStr):
    def __init__(self, value):
        super(Tags, self).__init__(value)

class AnswerCount(ColumnInt):
    def __init__(self, value):
        super(AnswerCount, self).__init__(value)

class CommentCount(ColumnInt):
    def __init__(self, value):
        super(CommentCount, self).__init__(value)

class FavoriteCount(ColumnInt):
    def __init__(self, value):
        super(FavoriteCount, self).__init__(value)

class ClosedDate(ColumnDate):
    def __init__(self, value):
        super(ClosedDate, self).__init__(value)

    def comment(self):
        s = '''present only if the post is closed'''
        return s

class CommunityOwnedDate(ColumnDate):
    def __init__(self, value):
        super(CommunityOwnedDate, self).__init__(value)

    def comment(self):
        s = '''present only if post is community wikied'''
        return s

if __name__ == '__main__':
    iidd = Id(1001)
    print iidd

    pti = PostTypeId(1002)
    print pti
    print pti.comment()

    cd = CreationDate('2009-03-05T22:28:34.823')
    print cd

    score = Score(99)
    print score

    vc = ViewCount(1003)
    print vc

    body = Body('<p>this is the &lt;body&gt; content</p>')
    print body

    oui = OwnerUserId(1)
    print oui
    print oui.comment()

    odn = OwnerDisplayName('Author Justin')
    print odn

    leui = LastEditorUserId('1005')
    print leui

    leun = LastEditorDisplayName('ELON MUSK')
    print leun

    led = LastEditDate('2009-03-05T22:28:34.823')
    print led

    lad = LastActivityDate('2009-03-11T12:51:01.480')
    print lad
    print lad.comment()

    title = Title('How to rm usr?')
    print title

    tags = Tags('unix,python,vim')
    print tags

    ac = AnswerCount(10)
    print ac

    cc = CommentCount(11)
    print cc

    fc = FavoriteCount(12)
    print fc

    cd = ClosedDate('2009-03-11T12:51:01.480')
    print cd

    cod = CommunityOwnedDate('2009-03-11T12:51:01.480')
    print cod


