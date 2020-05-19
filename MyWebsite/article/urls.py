from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import  static
from .views import *


urlpatterns = [

    path('',article_list,name='article_list'),
    path('<int:article_id>',article_detail,name='article_detail'),
    path('date/<int:year>/<int:month>',article_with_date,name="article_with_date" ),
    path('type/<int:tag_id>',article_with_type,name="article_with_type" ),

]