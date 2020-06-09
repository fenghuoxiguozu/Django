from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import LikeRecord
from django.utils.html import strip_tags
from notifications.signals import notify

@receiver(post_save,sender=LikeRecord)
def send_notification(sender,instance,**kwargs):
    recipient = instance.content_object.get_author()
    article = instance.content_object
    verb = '{}点赞了你的文章《{}》'.format(instance.user, article.title)
    notify.send(instance.user, recipient=recipient, verb=verb, action_object=instance)