# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-24 02:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20160124_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='posts.Post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 24, 2, 20, 11, 761977, tzinfo=utc)),
        ),
    ]
