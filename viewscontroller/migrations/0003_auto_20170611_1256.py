# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-11 12:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewscontroller', '0002_auto_20170611_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dayone',
            name='content',
            field=models.TextField(),
        ),
    ]
