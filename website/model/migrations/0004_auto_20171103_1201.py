# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-03 11:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0003_auto_20171103_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='countermeasure',
            name='id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='threat',
            name='id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]