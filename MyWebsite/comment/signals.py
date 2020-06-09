from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Comment
from django.utils.html import strip_tags
from notifications.signals import notify

@receiver(post_save,sender=Comment)
def send_notification(sender,instance,**kwargs):
    if instance.reply_to is None:  # 评论
        recipient = instance.content_object.get_author()
        if instance.content_type.model == 'article':
            article = instance.content_object
            verb = '{}评论了你的文章《{}》'.format(instance.user, article.title)
        else:
            raise Exception('unknown comment object type')
    else:  # 回复
        recipient = instance.reply_to
        verb = '{}回复了你的评论“{}”'.format(instance.user, strip_tags(instance.parent.commentText))
    notify.send(instance.user, recipient=recipient, verb=verb, action_object=instance)