# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 05:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bms_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_info',
            name='designation',
            field=models.CharField(default='Software Engineer', max_length=50),
        ),
    ]
