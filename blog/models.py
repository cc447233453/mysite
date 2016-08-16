from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField('title',max_length=200)
    content = models.TextField('content')
    create_time = models.DateTimeField('date published')