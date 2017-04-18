# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-17 11:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bms_app', '0022_remove_productuser_project_version'),
    ]

    operations = [
        migrations.CreateModel(
            name='BugStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='BugType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bug_name', models.CharField(max_length=50)),
            ],
        ),
    ]
