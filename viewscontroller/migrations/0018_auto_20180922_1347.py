# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-22 08:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewscontroller', '0017_auto_20180922_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbalance',
            name='balance',
            field=models.IntegerField(),
        ),
    ]
