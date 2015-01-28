#coding:utf-8
from django.db import models


class Novel(models.Model):
    '小说'

    INIT_STATUS = 0
    SERIAL_STATUS = 1 #连载中
    COMPLETE_STATUS = 2 #连载完毕
    ON_SYNC_STATUS = 3 #更新中
    NOVEL_STATUSES = (INIT_STATUS, SERIAL_STATUS, COMPLETE_STATUS, ON_SYNC_STATUS)
    WAITING_SYNC_STATUS = (INIT_STATUS, SERIAL_STATUS)

    id = models.CharField(u'id', max_length=32, primary_key=True) 
    name = models.CharField(u'名称', max_length=255, unique=True, db_index=True) 
    rule = models.CharField(u'章节标题规则', max_length=255, default='.+')
    createtime = models.PositiveIntegerField(u'创建时间', default=0, db_index=True) 
    updatetime = models.PositiveIntegerField(u'更新时间', default=0, db_index=True)
    status = models.SmallIntegerField(u'状态', default=0, db_index=True)

    class Meta(object):
        db_table = 'Novel' 

class Chapter(models.Model):
    '小说章节'

    UN_SYNC_STATUS = 0
    HAS_SYNC_STATUS = 1
    ON_SYNC_STATUS = 2

    WAITING_SYNC_STATUS = (UN_SYNC_STATUS, )

    id = models.CharField(u'id', max_length=32, primary_key=True) 
    novel = models.CharField(u'novel id', max_length=32, db_index=True) 
    title = models.CharField(u'名称', max_length=255, db_index=True)
    pageid = models.BigIntegerField(u'贴吧id', unique=True, db_index=True)
    createtime = models.PositiveIntegerField(u'创建时间', default=0, db_index=True) 
    updatetime = models.BigIntegerField(u'更新时间', default=0, db_index=True)
    status = models.SmallIntegerField(u'状态', default=0, db_index=True)
    content = models.TextField(u'内容', default='')

    class Meta(object):
        db_table = 'Chapter' 
