# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-26 20:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0002_auto_20170626_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]