from django.shortcuts import render,redirect
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.urls import reverse
from .models import *

def submitComment(request):
    user = request.user
    text = request.POST.get('commentText','')
    content_type = request.POST.get('content_type','')
    object_id = int(request.POST.get('object_id',''))
    print("pst:",content_type,object_id)
    model_class1 = ContentType.objects.get(model=content_type)
    print("model_class",model_class1)
    model_class = model_class1.model_class()
    model_object = model_class.objects.get(pk=object_id)

    comment = Comment()
    comment.user = user
    comment.commentText = text
    # comment.comment_time = timezone.now()
    comment.content_object = model_object
    comment.save()

    referer =request.META.get('HTTP_REFERER',reverse('index'))
    return redirect(referer)