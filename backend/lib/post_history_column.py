#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Justin<justinli.ljt@gmail.com>
# 2015-04-09

from base_column import *

#### column type - PostHistory ####

class Id(ColumnInt):
    def __init__(self, value):
        super(Id, self).__init__(value, empty=False)

class PostId(ColumnInt):
    def __init__(self, value):
        super(PostId, self).__init__(value, empty=False)

class PostHistoryTypeId(ColumnInt):
    def __init__(self, value):
        super(PostHistoryTypeId, self).__init__(value, empty=False)

    def comment(self):
        s = '''listed in the PostHistoryTypes table
            1. Initial Title - The first title a question is asked with.
            2. Initial Body - The first raw body text a post is submitted with.
            3. Initial Tags - The first tags a question is asked with.
            4. Edit Title - A question's title has been changed.
            5. Edit Body - A post's body has been changed, the raw text is stored here as markdown.
            6. Edit Tags - A question's tags have been changed.
            7. Rollback Title - A question's title has reverted to a previous version.
            8. Rollback Body - A post's body has reverted to a previous version - the raw text is stored here.
            9. Rollback Tags - A question's tags have reverted to a previous version.
            10. Post Closed - A post was voted to be closed.
            11. Post Reopened - A post was voted to be reopened.
            12. Post Deleted - A post was voted to be removed.
            13. Post Undeleted - A post was voted to be restored.
            14. Post Locked - A post was locked by a moderator.
            15. Post Unlocked - A post was unlocked by a moderator.
            16. Community Owned - A post has become community owned.
            17. Post Migrated - A post was migrated. superseded now with id 35 and 36 (away/here)
            18. Question Merged - A question has had another, deleted question merged into itself.
            19. Question Protected - A question was protected by a moderator.
            20. Question Unprotected - A question was unprotected by a moderator.
            21. Post Disassociated - An admin removes the OwnerUserId from a post.
            22. Question Unmerged - A previously merged question has had its answers and votes restored.
            24. Suggested Edit Applied
            25. Post Tweeted
            31. Comment discussion moved to chat
            33. Post notice added
            34. Post notice removed
            35. Post migrated away replaces id 17
            36. Post migrated here replaces id 17
            37. Post merge source
            38. Post merge destination'''
        return s

class RevisionGUID(ColumnStr):
    def __init__(self, value):
        super(RevisionGUID, self).__init__(value)

    def comment(self):
        s = '''At times more than one type of history record can be recorded by a single action. All of these will be grouped using the same RevisionGUID'''
        return s

class CreationDate(ColumnDate):
    def __init__(self, value):
        super(CreationDate, self).__init__(value)

class UserId(ColumnInt):
    def __init__(self, value):
        super(UserId, self).__init__(value, empty=False)

class UserDisplayName(ColumnStr):
    def __init__(self, value):
        super(UserDisplayName, self).__init__(value)

    def comment(self):
        s = '''populated if a user has been removed and no longer referenced by user Id'''
        return s

class Comment(ColumnStr):
    def __init__(self, value):
        super(Comment, self).__init__(value)

    def comment(self):
        s = '''This field will contain the comment made by the user who edited a post. If PostHistoryTypeId = 10, this field contains the CloseReasonId of the close reason (listed in CloseReasonTypes):
            Old close reasons:
            1: Exact Duplicate
            2: Off-topic
            3: Subjective and argumentative
            4: Not a real question
            7: Too localized
            10: General reference
            20: Noise or pointless (Meta sites only)
            Current close reasons:
            101: Duplicate
            102: Off-topic
            103: Unclear what you're asking
            104: Too broad
            105: Primarily opinion-based'''
        return s

class Text(ColumnStr):
    def __init__(self, value):
        super(Text, self).__init__(value)

    def comment(self):
        s = '''raw version of the new value for a given revision
                1. If PostHistoryTypeId = 10, 11, 12, 13, 14, or 15 this column will contain a JSON encoded string with all users who have voted for the PostHistoryTypeId
                2. If it is a duplicate close vote, the JSON string will contain an array of original questions as OriginalQuestionIds
                3. If PostHistoryTypeId = 17 this column will contain migration details of either from <url> or to <url>'''
        return s

if __name__ == '__main__':
    iidd = Id(1001)
    print iidd

    pi = PostId(1222)
    print pi

    phti = PostHistoryTypeId(1)
    print phti
    print phti.comment()

    rguid = RevisionGUID('fb15f802-f083-4474-affd-18b56226e611')
    print rguid
    print rguid.comment()

    cd = CreationDate('2009-03-05T22:28:34.823')
    print cd

    uid = UserId(1001)
    print uid
    print uid.comment()

    udn = UserDisplayName('Johnney')
    print udn

    comment = Comment('Unclear what you\'re asking')
    print comment
    print comment.comment()

    text = Text('{}')
    print text
    print text.comment()
