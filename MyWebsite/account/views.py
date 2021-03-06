from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout,get_user_model
from django.urls import reverse
from django.http import JsonResponse,HttpResponse
from .forms import *
from account.utils.captcha import GenCaptcha
from io import BytesIO
from django.core.mail import send_mail
from django.core.cache import cache
import random,string,time
# from like.models import LikeCount
User = get_user_model()


def img_captcha(request):
    text,image = GenCaptcha.gen_code()
    out = BytesIO()
    image.save(out,'png')
    out.seek(0)
    response = HttpResponse(content_type='image/png')
    response.write(out.read())
    response['Content-length'] = out.tell()
    cache.set(text.lower(),text.lower(),300)
    return response


def signIn(request):
    context = {}
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            login(request, user)
            return redirect(request.GET.get('from', reverse('index')))
    else:
        login_form = LoginForm()
    context['login_form'] = login_form
    return render(request, 'login.html', context)
        # if remember:
        #     request.session.set_expiry(60)
        # else:
        #     request.session.set_expiry(0)

def signUp(request):
    context = {}
    if request.method == 'POST':
        register_form = RegisterForm(request.POST,request=request)
        if register_form.is_valid():
            email = register_form.cleaned_data['email']
            password = register_form.cleaned_data['password']
            user = User.objects.create_user(email=email,password=password)
            user.save()
            del request.session['email_code']
            user = authenticate(email=email,password=password)
            login(request, user)
            return redirect(request.GET.get('from', reverse('index')))
    else:
        register_form = RegisterForm()
    context['register_form'] = register_form
    return render(request,'register.html',context)


def send_email(request):
    data={}
    email = request.GET.get('email','')
    email_code = request.GET.get('email_code','')

    code = ''.join(random.sample(string.ascii_letters+string.digits,4))
    now = int(time.time())
    email_code_time = request.session.get('email_code_time',0)
    if email != '':
        if now - email_code_time < 500:
            data['status'] = 'ERROR'
            data['message'] = '邮箱验证码发送太频繁，请60s后再尝试'
        else:
            request.session[email_code] = code
            request.session['email_code_time'] = now
            send_mail('绑定邮箱', '验证码%s'%code, '1058247664@qq.com',[email], fail_silently=False)
            data['status'] = 'SUCCESS'
            data['message'] = '邮箱验证码发送成功'
    else:
        data['status'] = 'ERROR'
    return JsonResponse(data)


def signOut(request):
    logout(request)
    return redirect(request.GET.get('from',reverse('index')))


def userInfo(request):
    # record = LikeCount.objects.filter(like_num=1,user=request.user)

    return render(request, 'userInfo.html')

def change_nickname(request):
    if request.method == "POST":
        nickname_form = NicknameForm(request.POST)
        if nickname_form.is_valid():
            nickname_new = nickname_form.cleaned_data['nickname_new']
            user = User.objects.get(email = request.user)
            user.nickname = nickname_new
            user.save()
            return redirect(request.META.get('HTTP_REFERER',reverse('index')))
    else:
        nickname_form = NicknameForm()
    context = {}
    context['form'] = nickname_form
    context['form_title'] = '修改昵称'
    return render(request, 'forms.html', context)

def change_sex(request):
    if request.method == "POST":
        form = SexForm(request.POST)
        if form.is_valid():
            sex = form.cleaned_data['sex']
            user = User.objects.get(email = request.user)
            user.sex = sex
            user.save()
            return redirect(request.META.get('HTTP_REFERER',reverse('index')))
    else:
        form = SexForm()
    context = {}
    context['form'] = form
    context['form_title'] = '修改性别'
    return render(request, 'forms.html', context)

def change_head(request):
    if request.method == "POST":
        form = HeadForm(request.POST,request.FILES)
        if form.is_valid():
            head = form.cleaned_data['head']
            user = User.objects.get(email=request.user)
            user.head = head
            user.save()
            return redirect(request.META.get('HTTP_REFERER',reverse('index')))
    else:
        form = HeadForm()
    context = {}
    context['form'] = form
    context['form_title'] = '修改头像'
    return render(request, 'forms.html', context)

def my_notifications(request):
    context = {}
    return render(request, 'my_notifications.html',context)

