# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-19 13:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bms_app', '0029_remove_bug_details_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='bug_details',
            name='dependent_module',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
