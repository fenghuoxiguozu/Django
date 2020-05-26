from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout,get_user_model
from django.urls import reverse
from .forms import LoginForm,RegisterForm,NicknameForm,EmailForm

User = get_user_model()

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


def signOut(request):
    logout(request)
    return redirect(request.GET.get('from',reverse('index')))


def userInfo(request):
    if request.method == "POST":
        nickname_form = NicknameForm(request.POST)
        if nickname_form.is_valid():
            nickname_new = nickname_form.cleaned_data['nickname_new']
            user = User.objects.get(username = request.user)
            user.nickname = nickname_new
            user.save()
            return redirect(request.GET.get('from', reverse('index')))
    else:
        nickname_form = NicknameForm()

    context = {}
    context['nickname_form'] = nickname_form

    return render(request, 'userInfo.html',context)

# def bind_email(request):
#     if request.method == "POST":
#         nickname_form = EmailForm(request.POST)
#         if nickname_form.is_valid():
#             nickname_new = nickname_form.cleaned_data['nickname_new']
#             user = User.objects.get(username = request.user)
#             user.nickname = nickname_new
#             user.save()
#             return redirect(request.GET.get('from', reverse('index')))
#     else:
#         nickname_form = NicknameForm()
#
#     context = {}
#     context['nickname_form'] = nickname_form
#
#     return render(request, 'userInfo.html',context)