# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-17 04:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gogleboks', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Review',
        ),
    ]