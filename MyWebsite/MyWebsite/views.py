from django.shortcuts import render,redirect
from django.contrib.contenttypes.models import ContentType
from read.utils import seven_days_readNum,hot_article
from article.models import Article
from django.core.cache import cache
from django.contrib.auth import login,authenticate
from django.urls import reverse
from .forms import LoginForm,RegisterForm
from django.contrib.auth.models import User

def index(request):
    context={}
    content_type = ContentType.objects.get_for_model(Article)
    dates_list,read_nums = seven_days_readNum(content_type=content_type)

    three_hot_articles = cache.get('three_hot_articles')
    seven_hot_articles = cache.get('seven_hot_articles')
    thirty_hot_articles = cache.get('thirty_hot_articles')
    if three_hot_articles is None:
        three_hot_articles = hot_article(3)
        seven_hot_articles = hot_article(7)
        thirty_hot_articles = hot_article(30)
        cache.set('three_hot_articles',three_hot_articles,3600)
        cache.set('seven_hot_articles', seven_hot_articles,3600)
        cache.set('thirty_hot_articles', seven_hot_articles,3600)

    context['read_nums'] = read_nums
    context['dates_list'] = dates_list
    context['three_hot_articles'] = three_hot_articles
    context['seven_hot_articles'] = seven_hot_articles
    context['thirty_hot_articles'] = thirty_hot_articles
    return render(request,'chart.html',context)


def signIn(request):
    context={}
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            login(request,user)
            return redirect(request.GET.get('from',reverse('index')))
    else:
        login_form = LoginForm()
    context['login_form'] = login_form
    return render(request, 'login.html',context)


def signUp(request):
    context={}
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password = register_form.cleaned_data['password']
            email = register_form.cleaned_data['email']
            user = User.objects.create_user(username,email,password)
            user.save()
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect(request.GET.get('from',reverse('index')))
    else:
        register_form = RegisterForm()
    context['register_form'] = register_form
    return render(request, 'register.html',context)

