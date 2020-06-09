from django.shortcuts import render
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse
from .models import *
from django.db.models import Sum
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
    data['like_num'] = like_num or 0
    return JsonResponse(data)

def likeChange(request):
    user = request.user
    if not user.is_authenticated:
        return ErrorResponse(400, 'you were not login')

    content_type = request.GET.get('content_type')
    object_id = int(request.GET.get('object_id'))
    is_like = request.GET.get('is_like')

    content_type = ContentType.objects.get(model=content_type)

    # record = LikeRecord.objects.create(content_type=content_type, object_id=object_id, user=user)
    # counted, created = LikeCount.objects.get_or_create(content_type=content_type, object_id=object_id,user=user)


    if is_like == 'true':
        record, created = LikeRecord.objects.get_or_create(content_type=content_type, object_id=object_id, user=user)
        if created:
            print("created",record.like_num)
            record.like_num = 1
            record.save()
        else:
            pass
    else:
        record = LikeRecord.objects.get(content_type=content_type, object_id=object_id, user=user)
        print("exist()", record.like_num)
        record.delete()
        # record.save()
    # like_num = LikeRecord.objects.filter(content_type=content_type, object_id=object_id, user=user).count()%2
    like_counts = LikeRecord.objects.filter(object_id=object_id).aggregate(counts=Sum('like_num'))
    print('like_counts:',like_counts)
    return SuccessResponse(like_counts['counts'])




