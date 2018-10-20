# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import userBalance,userInfo,isApproved
admin.site.register(userBalance)
admin.site.register(userInfo)
admin.site.register(isApproved)
