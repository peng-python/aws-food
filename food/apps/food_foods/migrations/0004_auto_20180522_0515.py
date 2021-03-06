# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-22 05:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_foods', '0003_auto_20180522_0241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodblogmodel',
            name='image',
            field=models.ImageField(upload_to='blog/image/%Y/%m/', verbose_name='文章图片'),
        ),
        migrations.AlterField(
            model_name='foodexplainmodel',
            name='image',
            field=models.ImageField(upload_to='explain/%Y/%m/', verbose_name='说明图片'),
        ),
        migrations.AlterField(
            model_name='foodshowmodel',
            name='image',
            field=models.ImageField(upload_to='introduce/%Y/%m/', verbose_name='展示图片'),
        ),
        migrations.AlterField(
            model_name='homepicmodel',
            name='image',
            field=models.ImageField(max_length=500, upload_to='pic/%Y/%m/', verbose_name='主页图片'),
        ),
    ]
