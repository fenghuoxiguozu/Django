from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse
from .models import *
# Create your views here.

def ErrorResponse(code, message):
    data = {}
    data['status'] = 'ERROR'
    data['code'] = code
    data['message'] = message
    return JsonResponse(data)

def SuccessResponse(like_num):
    data = {}
    data['status'] = 'SUCCESS'
    data['like_num'] = like_num
    return JsonResponse(data)

def likeChange(request):
    user = request.user
    content_type = request.GET.get('content_type')
    object_id = int(request.GET.get('object_id'))
    is_like = request.GET.get('is_like')

    content_type = ContentType.objects.get(model=content_type)
    # model_class = content_type.model_class()
    # model_obj = model_class.objects.get(pk=object_id)

    record = LikeRecord.objects.create(content_type=content_type, object_id=object_id, user=user)
    counted, created = LikeCount.objects.get_or_create(content_type=content_type, object_id=object_id)
    if is_like == 'true':
        counted.like_num = 1
    else:
        counted.like_num = 0
    counted.save()
    record.save()
    like_num = LikeRecord.objects.filter(content_type=content_type, object_id=object_id, user=user).count()%2
    return SuccessResponse(like_num)




