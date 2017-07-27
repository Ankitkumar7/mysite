# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import dayOne, dayTwo, dayThree, dayFour, dayFive, daySix, music
# Register your models here.
admin.site.register(dayOne)
admin.site.register(dayTwo)
admin.site.register(dayThree)
admin.site.register(dayFour)
admin.site.register(dayFive)
admin.site.register(daySix)
admin.site.register(music)