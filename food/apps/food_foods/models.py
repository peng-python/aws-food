from django.db import models
from datetime import datetime

from DjangoUeditor.models import UEditorField
from users.models import UserProfile

# Create your models here.


class HomePicModel(models.Model):
    title = models.CharField(max_length=100, verbose_name='图片标题')
    image = models.ImageField(upload_to='pic/%Y/%m/', max_length=500, verbose_name='主页图片')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '首页图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class FoodAboutModel(models.Model):
    title = models.CharField(max_length=100, verbose_name='介绍标题')
    content = models.TextField(verbose_name='内容')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '首页关于介绍'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class FoodShowModel(models.Model):
    title = models.CharField(max_length=100, verbose_name='展示图片标题')
    image = models.ImageField(upload_to='introduce/%Y/%m/', verbose_name='展示图片')
    content = models.TextField(verbose_name='展示文字内容')
    # place = models.CharField(choices=(('fadeInLeft', '左边'), ('fadeInUp', '中间'), ('fadeInLeft')))
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '首页展示'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class FoodServicesModel(models.Model):
    title = models.CharField(max_length=100, verbose_name='服务标题')
    content = models.TextField(verbose_name='内容')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '服务内容(简单说明)'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class FoodExplainModel(models.Model):
    title = models.CharField(max_length=200, verbose_name='说明标题')
    content = models.TextField(max_length=500, verbose_name='说明内容')
    image = models.ImageField(upload_to='explain/%Y/%m/', verbose_name='说明图片')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '服务说明'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class FoodNewModel(models.Model):
    title = models.CharField(max_length=100, verbose_name='新文章介绍标题')
    content = models.TextField(max_length=500, verbose_name='新文章介绍内容')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '新文章介绍内容'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class FoodBlogModel(models.Model):
    title = models.CharField(max_length=100, verbose_name='文章标题')
    content = UEditorField(verbose_name='文章内容', width=600, height=300,
                           imagePath='blog/ueditor/%%Y/%%m/', filePath='blog/ueditor/%%Y/%%m/')
    title_image = models.ImageField(upload_to='blog/image/%Y/%m/', verbose_name='文章标题图片', default='')
    image = models.ImageField(upload_to='blog/image/%Y/%m/', verbose_name='文章图片')
    category = models.CharField(choices=(('Chinese', '中餐'), ('Western_style', '西餐'), ('snack', '小食'),
                                         ('event', '美食界的事件')), verbose_name='分类', max_length=50)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class FoodCommentModel(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户')
    blog = models.ForeignKey(FoodBlogModel, verbose_name='文章')
    comment = models.TextField(max_length=500, verbose_name='评论内容')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.blog.title