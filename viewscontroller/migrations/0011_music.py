# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 10:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewscontroller', '0010_auto_20170625_0800'),
    ]

    operations = [
        migrations.CreateModel(
            name='music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=2000)),
            ],
        ),
    ]
