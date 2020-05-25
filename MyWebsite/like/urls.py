from django.urls import path
from .views import likeChange

urlpatterns = [
    path('likeChange',likeChange,name='likeChange'),
]