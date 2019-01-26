# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Article(models.Model):
    # AttributeError:'module' object has no attribute 'Charfield'错误
    # 注意应该是大小写的问题：CharField才对。
    # title = models.charField(max_length=32, default='Title')
    title = models.CharField(max_length=32, default='Title')
    content = models.TextField(null=True)
    pub_time = models.DateTimeField(null=True)

    def __unicode__(self):
        return self.title