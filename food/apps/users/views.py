from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout

from .forms import RegisterForm, LoginForm
from .models import UserProfile

# Create your views here.


def register_user(request):
    request_form = RegisterForm(request.POST)
    if request_form.is_valid():
        post = request.POST
        user_name = post.get('user_name', '')
        pass_word = post.get('pass_word', '')
        email = post.get('email', '')
        mobile = post.get('mobile', '')
        message = post.get('message', '')
        users = UserProfile()
        users.username = user_name
        users.nick_name = user_name
        users.password = make_password(pass_word)
        users.email = email
        users.mobile = mobile
        users.message = message
        users.save()
        return render(request, 'login.html')
    else:
        return render(request, 'register.html')


def login_user(request):
    login_form = LoginForm(request.POST)
    if login_form.is_valid():
        post = request.POST
        user_name = post.get('user_name', '')
        pass_word = post.get('pass_word', '')
        user = authenticate(username=user_name, password=pass_word)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def page_not_found(request):
    from django.shortcuts import render_to_response
    response = render_to_response('404.html', {})
    response.status_code = 404
    return response