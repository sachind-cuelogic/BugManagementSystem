# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-16 17:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bms_app', '0038_auto_20170503_0456'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='comment_tme',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
