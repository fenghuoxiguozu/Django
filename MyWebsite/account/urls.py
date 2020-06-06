from django.urls import path
from .views import *

urlpatterns = [
    path('login',signIn,name='login'),
    path('register',signUp,name='register'),
    path('logout',signOut,name='logout'),
    path('captcha/', img_captcha,name='img_captcha'),
    path('send_email',send_email,name='send_email'),
    path('userInfo',userInfo,name='userInfo'),
    path('change_nickname',change_nickname,name='change_nickname'),
    path('change_sex',change_sex,name='change_sex'),
    path('change_head',change_head,name='change_head'),
]