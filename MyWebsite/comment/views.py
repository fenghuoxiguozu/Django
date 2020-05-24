from django.shortcuts import render,redirect
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
import time
from django.http import JsonResponse
from .models import *
from article.forms import CommentForm

def submit(request):
    # referer =request.META.get('HTTP_REFERER',reverse('index'))
    comment_form = CommentForm(request.POST,user=request.user)
    if comment_form.is_valid():
        comment = Comment()
        comment.user = comment_form.cleaned_data['user']
        comment.commentText = comment_form.cleaned_data['commentText']
        comment.content_object = comment_form.cleaned_data['content_object']
        parent = comment_form.cleaned_data['parent']
        if not parent is None:
            comment.root = parent.root if not parent.root is None else parent
            comment.parent = parent
            comment.reply_to = parent.user

        comment.save()
        response_dict={"user":comment.user.username,"commentText":comment.commentText,
                       "commentTime":comment.commentTime.strftime('%Y-%m-%d %H:%M:%S'),"status":"SUCCESS",'pk':comment.pk,
                       'root_pk':comment.root.pk if not comment.root is None else '',
                       'reply_to':comment.reply_to.username if not parent is None else ''}
        # return redirect(referer)
    else:
        # return render(request,'error.html',{"message":comment_form.errors,"redirect_to":referer})
        response_dict={"status":"ERROR"}
    return JsonResponse(response_dict)