from django.shortcuts import render,redirect
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.http import JsonResponse
from django.utils.html import strip_tags
from .models import *
from article.forms import CommentForm
from notifications.signals import notify

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
        response_dict={"user":comment.user.uid,"commentText":comment.commentText,
                       "commentTime":comment.commentTime.strftime('%Y-%m-%d %H:%M:%S'),
                       "status":"SUCCESS",'pk':comment.pk,
                       'root_pk':comment.root.pk if not comment.root is None else '',
                       'reply_to':comment.reply_to.uid if not parent is None else ''}

        # if comment.reply_to is None:    # 评论
        #     recipient = comment.content_object.get_author()
        #     if comment.content_type.model == 'article':
        #         article = comment.content_object
        #         verb = '{}评论了你的文章《{}》'.format(comment.user,article.title)
        #     else:
        #         raise Exception('unknown comment object type')
        # else:   # 回复
        #     recipient = comment.reply_to
        #     verb = '{}回复了你的评论“{}”'.format(comment.user,strip_tags(comment.parent.commentText))
        # notify.send(comment.user,recipient=recipient,verb=verb,action_object=comment)

        # return redirect(referer)
    else:
        # return render(request,'error.html',{"message":comment_form.errors,"redirect_to":referer})
        response_dict={"status":"ERROR"}
    return JsonResponse(response_dict)