# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-22 08:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewscontroller', '0018_auto_20180922_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbalance',
            name='balance',
            field=models.IntegerField(default=0),
        ),
    ]
