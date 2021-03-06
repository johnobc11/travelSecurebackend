# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class cities(models.Model):
    tweet_id = models.BigIntegerField(blank=True)
    tweet_timestamp = models.CharField(blank=True, max_length=200)
    tweet_screenname = models.CharField(blank=True, max_length=200)
    tweet_favour_count = models.CharField(blank=True, max_length=200)
    tweet_recount = models.BigIntegerField(blank=True)
    tweet_location = models.CharField(blank=True, null=True, max_length=200)
    tweet_text = models.TextField(blank=True)
    tweet_status = models.TextField(blank=True)
    tweet_score = models.TextField(blank=True)
    tweet_media_entities = models.URLField(blank=True)
    theCountry = models.TextField(blank=True)
    theCity = models.TextField(blank=True)
    dangerLevel = models.IntegerField(blank=True)