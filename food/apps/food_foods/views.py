from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.core.cache import cache
from django.views.decorators.cache import cache_page

from .models import HomePicModel, FoodAboutModel, FoodShowModel, FoodExplainModel, \
    FoodBlogModel, FoodCommentModel, FoodServicesModel, FoodNewModel

# Create your views here.


def get_blog_cache():
    new_blog = cache.get('new_list')
    if new_blog is None:
        new_blog = FoodBlogModel.objects.all().order_by('id')[:3]
        cache.set('new_list', new_blog)
        new_blog = cache.get('new_list', 20)
    return new_blog


class IndexView(View):
    def get(self, request):
        home_pic = HomePicModel.objects.last()
        about_content = FoodAboutModel.objects.last()
        about_show = FoodShowModel.objects.all().order_by('-id')[:3]
        list1 = ['fadeInUp', 'fadeInLeft', 'fadeInDown']
        explain = FoodExplainModel.objects.all().order_by('-id')[:3]
        blogs = FoodBlogModel.objects.all().order_by('-id')[:2]
        list2 = ['fadeInUp', 'fadeInRight', 'fadeInLeft', 'fadeInDown']
        service = FoodServicesModel.objects.last()
        news = FoodNewModel.objects.last()
        context = {'about_show': about_show, 'home_pic': home_pic, 'list1': list1, 'explain': explain,
                   'blogs': blogs, 'list2': list2, 'about_content': about_content, 'service': service, 'news': news}
        return render(request, 'index.html', context)


def blog(request):
    blogs = FoodBlogModel.objects.all().order_by('-id')
    new_blogs = get_blog_cache()
    try:
        page = request.GET.get('page', '1')
    except PageNotAnInteger:
        page = 1
    p = Paginator(blogs, 6, request=request)
    blogs = p.page(page)
    context = {'blogs': blogs, 'new_blogs': new_blogs}
    return render(request, 'blog.html', context)


@cache_page(20)
def detail(request, blog_id):
    blog = FoodBlogModel.objects.get(id=int(blog_id))
    comments = FoodCommentModel.objects.filter(blog_id=int(blog_id))
    comments1 = comments.order_by('-id')
    new_blogs = get_blog_cache()
    list1 = ['fadeInLeft', 'fadeInUp', 'fadeInRight']
    comment_nums = comments.count()
    context = {'blog': blog, 'comments': comments1, 'list1': list1, 'new_blogs': new_blogs, 'comment_nums': comment_nums}
    return render(request, 'detail.html', context)


def comment(request):
    if not request.user.is_authenticated():
        return HttpResponse('{"status":"fail","msg":"用户未登录"}', content_type='application/json')
    blog_id = request.POST.get('blog_id', 0)
    comment = request.POST.get('comment', '')
    if comment:
        blog_comment = FoodCommentModel()
        blog = FoodBlogModel.objects.get(id=int(blog_id))
        blog_comment.blog = blog
        blog_comment.comment = comment
        blog_comment.user = request.user
        blog_comment.save()
        return HttpResponse('{"status":"success","msg":"添加成功"}', content_type='application/json')
    else:
        return HttpResponse('{"status":"fail","msg":"添加失败"}', content_type='application/json')
