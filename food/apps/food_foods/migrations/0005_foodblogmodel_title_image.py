# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-27 21:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_foods', '0004_auto_20180522_0515'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodblogmodel',
            name='title_image',
            field=models.ImageField(default='', upload_to='blog/image/%Y/%m/', verbose_name='文章标题图片'),
        ),
    ]
