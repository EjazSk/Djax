# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils.timesince import timesince


# Create your models here.
class TweetModel(models.Model):
	user = models.ForeignKey(User)
	content = models.CharField(max_length=180)
	timestamp  = models.DateTimeField(auto_now_add	=True)
	updated = models.DateTimeField(auto_now=True)


	def __str__(self):
		return str(self.content)

	def FORMAT(self):
		return timesince(self.timestamp)
	class Meta:
		ordering=['-id',]