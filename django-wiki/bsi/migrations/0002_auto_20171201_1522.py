# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-01 15:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bsi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articleattr',
            name='article',
        ),
        migrations.RemoveField(
            model_name='articleattr',
            name='reference_id',
        ),
        migrations.DeleteModel(
            name='ArticleAttr',
        ),
    ]