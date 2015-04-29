# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.

# cmd: python manage.py inspectdb

from __future__ import unicode_literals

from django.db import models


class Badges(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True) 
    userid = models.IntegerField(db_column='UserId', blank=True, null=True) 
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True) 
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True) 

    class Meta:
        managed = False
        db_table = 'badges'
        app_label = 'posts'


class Comments(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True) 
    postid = models.IntegerField(db_column='PostId') 
    score = models.IntegerField(db_column='Score') 
    text = models.TextField(db_column='Text', blank=True, null=True) 
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True) 
    userid = models.IntegerField(db_column='UserId') 

    class Meta:
        managed = False
        db_table = 'comments'
        app_label = 'posts'


class PostHistory(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True) 
    posthistorytypeid = models.SmallIntegerField(db_column='PostHistoryTypeId') 
    postid = models.IntegerField(db_column='PostId') 
    revisionguid = models.CharField(db_column='RevisionGUID', max_length=36, blank=True, null=True) 
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True) 
    userid = models.IntegerField(db_column='UserId') 
    text = models.TextField(db_column='Text', blank=True, null=True) 

    class Meta:
        managed = False
        db_table = 'post_history'
        app_label = 'posts'


class Posts(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True) 
    posttypeid = models.SmallIntegerField(db_column='PostTypeId', blank=True, null=True) 
    acceptedanswerid = models.IntegerField(db_column='AcceptedAnswerId', blank=True, null=True) 
    parentid = models.IntegerField(db_column='ParentId', blank=True, null=True) 
    score = models.IntegerField(db_column='Score', blank=True, null=True) 
    viewcount = models.IntegerField(db_column='ViewCount', blank=True, null=True) 
    body = models.TextField(db_column='Body', blank=True, null=True) 
    owneruserid = models.IntegerField(db_column='OwnerUserId') 
    lasteditoruserid = models.IntegerField(db_column='LastEditorUserId', blank=True, null=True) 
    lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True) 
    lastactivitydate = models.DateTimeField(db_column='LastActivityDate', blank=True, null=True) 
    title = models.CharField(db_column='Title', max_length=256) 
    tags = models.CharField(db_column='Tags', max_length=256, blank=True, null=True) 
    answercount = models.IntegerField(db_column='AnswerCount') 
    commentcount = models.IntegerField(db_column='CommentCount') 
    favoritecount = models.IntegerField(db_column='FavoriteCount') 
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True) 

    class Meta:
        managed = False
        db_table = 'posts'
        app_label = 'posts'


class Posts1(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True) 
    posttypeid = models.SmallIntegerField(db_column='PostTypeId', blank=True, null=True) 
    acceptedanswerid = models.IntegerField(db_column='AcceptedAnswerId', blank=True, null=True) 
    parentid = models.IntegerField(db_column='ParentId', blank=True, null=True) 
    score = models.IntegerField(db_column='Score', blank=True, null=True) 
    viewcount = models.IntegerField(db_column='ViewCount', blank=True, null=True) 
    body = models.TextField(db_column='Body', blank=True, null=True) 
    owneruserid = models.IntegerField(db_column='OwnerUserId') 
    lasteditoruserid = models.IntegerField(db_column='LastEditorUserId', blank=True, null=True) 
    lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True) 
    lastactivitydate = models.DateTimeField(db_column='LastActivityDate', blank=True, null=True) 
    title = models.CharField(db_column='Title', max_length=256) 
    tags = models.CharField(db_column='Tags', max_length=256, blank=True, null=True) 
    answercount = models.IntegerField(db_column='AnswerCount') 
    commentcount = models.IntegerField(db_column='CommentCount') 
    favoritecount = models.IntegerField(db_column='FavoriteCount') 
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True) 

    class Meta:
        managed = False
        db_table = 'posts_1'
        app_label = 'posts'


class Posts2(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True) 
    posttypeid = models.SmallIntegerField(db_column='PostTypeId', blank=True, null=True) 
    acceptedanswerid = models.IntegerField(db_column='AcceptedAnswerId', blank=True, null=True) 
    parentid = models.IntegerField(db_column='ParentId', blank=True, null=True) 
    score = models.IntegerField(db_column='Score', blank=True, null=True) 
    viewcount = models.IntegerField(db_column='ViewCount', blank=True, null=True) 
    body = models.TextField(db_column='Body', blank=True, null=True) 
    owneruserid = models.IntegerField(db_column='OwnerUserId') 
    lasteditoruserid = models.IntegerField(db_column='LastEditorUserId', blank=True, null=True) 
    lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True) 
    lastactivitydate = models.DateTimeField(db_column='LastActivityDate', blank=True, null=True) 
    title = models.CharField(db_column='Title', max_length=256) 
    tags = models.CharField(db_column='Tags', max_length=256, blank=True, null=True) 
    answercount = models.IntegerField(db_column='AnswerCount') 
    commentcount = models.IntegerField(db_column='CommentCount') 
    favoritecount = models.IntegerField(db_column='FavoriteCount') 
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True) 

    class Meta:
        managed = False
        db_table = 'posts_2'
        app_label = 'posts'


class Posts3(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True) 
    posttypeid = models.SmallIntegerField(db_column='PostTypeId', blank=True, null=True) 
    acceptedanswerid = models.IntegerField(db_column='AcceptedAnswerId', blank=True, null=True) 
    parentid = models.IntegerField(db_column='ParentId', blank=True, null=True) 
    score = models.IntegerField(db_column='Score', blank=True, null=True) 
    viewcount = models.IntegerField(db_column='ViewCount', blank=True, null=True) 
    body = models.TextField(db_column='Body', blank=True, null=True) 
    owneruserid = models.IntegerField(db_column='OwnerUserId') 
    lasteditoruserid = models.IntegerField(db_column='LastEditorUserId', blank=True, null=True) 
    lasteditdate = models.DateTimeField(db_column='LastEditDate', blank=True, null=True) 
    lastactivitydate = models.DateTimeField(db_column='LastActivityDate', blank=True, null=True) 
    title = models.CharField(db_column='Title', max_length=256) 
    tags = models.CharField(db_column='Tags', max_length=256, blank=True, null=True) 
    answercount = models.IntegerField(db_column='AnswerCount') 
    commentcount = models.IntegerField(db_column='CommentCount') 
    favoritecount = models.IntegerField(db_column='FavoriteCount') 
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True) 

    class Meta:
        managed = False
        db_table = 'posts_3'
        app_label = 'posts'


class Users(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True) 
    reputation = models.IntegerField(db_column='Reputation') 
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True) 
    displayname = models.CharField(db_column='DisplayName', max_length=50, blank=True, null=True) 
    lastaccessdate = models.DateTimeField(db_column='LastAccessDate', blank=True, null=True) 
    views = models.IntegerField(db_column='Views', blank=True, null=True) 
    websiteurl = models.CharField(db_column='WebsiteUrl', max_length=256, blank=True, null=True) 
    location = models.CharField(db_column='Location', max_length=256, blank=True, null=True) 
    aboutme = models.TextField(db_column='AboutMe', blank=True, null=True) 
    age = models.IntegerField(db_column='Age', blank=True, null=True) 
    upvotes = models.IntegerField(db_column='UpVotes', blank=True, null=True) 
    downvotes = models.IntegerField(db_column='DownVotes', blank=True, null=True) 
    emailhash = models.CharField(db_column='EmailHash', max_length=32, blank=True, null=True) 

    class Meta:
        managed = False
        db_table = 'users'
        app_label = 'posts'


class Votes(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True) 
    postid = models.IntegerField(db_column='PostId') 
    votetypeid = models.SmallIntegerField(db_column='VoteTypeId', blank=True, null=True) 
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True) 

    class Meta:
        managed = False
        db_table = 'votes'
        app_label = 'posts'

class MetaTag(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    sum = models.IntegerField(db_column='Sum', blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=256)
    excerpt = models.CharField(db_column='Excerpt', max_length=512)
    wiki = models.TextField(db_column='Wiki', blank=True, null=True)
    md5 = models.CharField(db_column='MD5', max_length=32)

    class Meta:
        managed = False
        db_table = 'meta_tag'
        app_label = 'posts'



