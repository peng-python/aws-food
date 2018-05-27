from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, default='', verbose_name='昵称')
    mobile = models.CharField(max_length=11, default='', verbose_name='手机号码')
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name='邮箱')
    message = models.TextField(verbose_name='消息', null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username