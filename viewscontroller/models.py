# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class userBalance(models.Model):
    balance = models.IntegerField()
    user = models.ForeignKey(User, unique=True)
    def __unicode__(self):
        return str(self.user)