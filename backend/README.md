# Backend scripts

###I Module - Store
1. read dump xml file
1. parse columns of each row
1. store(insert) into RDS of aliyun

#### DB tables of Posts data 
table | start id | end id | count |
:----:|----------|--------|-------|
posts|4|5885813|5000000
posts_1|5885814|11705307|5000000
posts_2|11705308|17537162|5000000
posts_3|17537164|18657320|979180
_p.s.: stackoverflow@stackexchange.mysql.rds.aliyuncs.com:3306_

#### Class Inheritance of store
* parent: Store
* child: Posts PostHistory Votes Comments Users Badges 

####Usage
    python posts.py [posts_xml_file] [start=0] [end=intmax]
    python posts.py ~/Downloads/stackoverflow-data-dump-from-MEGA/stackoverflow.com.7z/Posts.xml 15001 1000000

###II Module - Translate
1. translate title with Google periodly
2. store into db



----
_powered by Mou_
