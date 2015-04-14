#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Justin<justinli.ljt@gmail.com>
# 2015-04-09

from base_column import *

#### column type - Votes ####

class Id(ColumnInt):
    def __init__(self, value):
        super(Id, self).__init__(value, empty=False)

class PostId(ColumnInt):
    def __init__(self, value):
        super(PostId, self).__init__(value, empty=False)

class VoteTypeId(ColumnInt):
    def __init__(self, value):
        super(VoteTypeId, self).__init__(value)

    def comment(self):
        s = '''listed in the VoteTypes table
            1 - AcceptedByOriginator
            2 - UpMod
            3 - DownMod
            4 - Offensive
            5 - Favorite (UserId will also be populated)
            6 - Close
            7 - Reopen
            8 - BountyStart (UserId and BountyAmount will also be populated)
            9 - BountyClose (BountyAmount will also be populated)
            10 - Deletion
            11 - Undeletion
            12 - Spam
            15 - ModeratorReview  
            16 - ApproveEditSuggestion'''
        return s

class UserId(ColumnInt):
    def __init__(self, value):
        super(UserId, self).__init__(value, empty=False)

    def comment(self):
        s = '''only present if VoteTypeId is 5 or 8'''
        return s

class CreationDate(ColumnDate):
    def __init__(self, value):
        super(CreationDate, self).__init__(value)

class BountyAmount(ColumnInt):
    def __init__(self, value):
        super(BountyAmount, self).__init__(value, empty=False)

    def comment(self):
        s = '''only present if VoteTypeId is 8 or 9'''
        return s

if __name__ == '__main__':
    iidd = Id(1001)
    print iidd

    pi = PostId(1222)
    print pi

    vti = VoteTypeId(8)
    print vti
    print vti.comment()

    uid = UserId(1001)
    print uid
    print uid.comment()

    cd = CreationDate('2009-03-05T22:28:34.823')
    print cd

    ba = BountyAmount(10000)
    print ba
    print ba.comment()

