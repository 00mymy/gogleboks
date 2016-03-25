# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-22 04:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gogleboks', '0002_auto_20160317_1307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='author',
            new_name='reviewer',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='published_date',
            new_name='updated_date',
        ),
        migrations.RemoveField(
            model_name='review',
            name='book',
        ),
        migrations.AddField(
            model_name='review',
            name='authors',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='review',
            name='bid',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='review',
            name='score',
            field=models.IntegerField(choices=[(1, '완전비추)'), (2, '쫌...비추'), (3, '보통'), (4, '괜찮음'), (5, '완전강추')], default=0),
        ),
        migrations.AddField(
            model_name='review',
            name='subtitle',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]
