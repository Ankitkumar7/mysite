# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-25 14:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_auto_20181125_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testerstatus',
            name='timestamp',
            field=models.DateTimeField(default=b'2018-11-25 19H:47M[:25S[.205000]]'),
        ),
        migrations.AlterField(
            model_name='uatstatus',
            name='timestamp',
            field=models.DateTimeField(default=b'2018-11-25 19H:47M[:25S[.206000]]'),
        ),
    ]