from django.urls import path
from .views import *

urlpatterns = [
    path('login',signIn,name='login'),
    path('register',signUp,name='register'),
    path('logout',signOut,name='logout'),
    path('userInfo',userInfo,name='userInfo'),
    # path('nickname',change_nickname,name='change_nickname'),
]