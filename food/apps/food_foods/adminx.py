import xadmin

from .models import HomePicModel, FoodAboutModel, FoodShowModel, FoodServicesModel, \
    FoodExplainModel, FoodBlogModel, FoodCommentModel, FoodNewModel


class HomePicAdmin(object):
    list_display = ['title', 'add_time']
    list_filter = ['title']
    search_fields = ['title', 'add_time']


class FoodAboutAdmin(object):
    list_display = ['title', 'content', 'add_time']
    list_filter = ['title', 'content']
    search_fields = ['title', 'content', 'add_time']


class FoodShowAdmin(object):
    list_display = ['title', 'content', 'add_time']
    list_filter = ['title', 'content']
    search_fields = ['title', 'content', 'add_time']


class FoodServicesAdmin(object):
    list_display = ['title', 'content', 'add_time']
    list_filter = ['title', 'content']
    search_fields = ['title', 'content', 'add_time']


class FoodExplainAdmin(object):
    list_display = ['title', 'content', 'add_time']
    list_filter = ['title', 'content']
    search_fields = ['title', 'content', 'add_time']


class FoodBlogAdmin(object):
    list_display = ['title', 'content', 'category', 'add_time']
    list_filter = ['title', 'content', 'category']
    search_fields = ['title', 'content', 'category', 'add_time']
    style_fields = {'content': 'ueditor'}


class FoodCommentAdmin(object):
    list_display = ['user', 'blog', 'comment', 'add_time']
    list_filter = ['user', 'blog', 'comment', 'add_time']
    search_fields = ['user', 'blog', 'comment', 'add_time']


class FoodNewAdmin(object):
    list_display = ['title', 'content', 'add_time']
    list_filter = ['title', 'content', 'add_time']
    search_fields = ['title', 'content', 'add_time']


xadmin.site.register(HomePicModel, HomePicAdmin)
xadmin.site.register(FoodAboutModel, FoodAboutAdmin)
xadmin.site.register(FoodShowModel, FoodShowAdmin)
xadmin.site.register(FoodServicesModel, FoodServicesAdmin)
xadmin.site.register(FoodExplainModel, FoodExplainAdmin)
xadmin.site.register(FoodBlogModel, FoodBlogAdmin)
xadmin.site.register(FoodCommentModel, FoodCommentAdmin)
xadmin.site.register(FoodNewModel, FoodNewAdmin)