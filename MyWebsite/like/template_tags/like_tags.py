from django import template
from django.contrib.contenttypes.models import ContentType
from like.models import *

register = template.Library()

@register.simple_tag
def like_counts(obj):
    content_type = ContentType.objects.get_for_model(obj)
    like_count = LikeRecord.objects.filter(content_type=content_type,object_id=obj.pk).count()
    return like_count.like_num


