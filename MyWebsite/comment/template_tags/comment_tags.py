from django import template
from django.contrib.contenttypes.models import ContentType
from comment.models import Comment
from article.forms import CommentForm
from like.models import *

register = template.Library()

@register.simple_tag
def comment_counts(obj):
    content_type = ContentType.objects.get_for_model(obj)
    return Comment.objects.filter(content_type=content_type,object_id=obj.pk).count()


@register.simple_tag
def comment_form(obj):
    content_type = ContentType.objects.get_for_model(obj)
    form = CommentForm(initial={'content_type': content_type.model, 'object_id': obj.pk, 'reply_id': 0})
    return form


@register.simple_tag
def comment_list(obj):
    content_type = ContentType.objects.get_for_model(obj)
    all_comments = Comment.objects.filter(content_type=content_type, object_id=obj.pk, parent=None)
    return all_comments.order_by('-commentTime')

from django.db.models import Count
@register.simple_tag()
def like_counts(obj):
    content_type = ContentType.objects.get_for_model(obj)
    like_count, created = LikeCount.objects.get_or_create(content_type=content_type, object_id=obj.pk)
    return like_count.like_num


@register.simple_tag(takes_context=True)
def like_status(context, obj):
    content_type = ContentType.objects.get_for_model(obj)
    user = context['user']
    if not user.is_authenticated:
        return ''
    sums = LikeRecord.objects.filter(content_type=content_type, object_id=obj.pk, user=user).count()
    if sums%2 == 1:
        return 'active'
    else:
        return ''
