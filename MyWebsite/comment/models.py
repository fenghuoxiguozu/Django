from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.conf import settings
# Create your models here.

class Comment(models.Model):
    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type','object_id')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments',on_delete=models.CASCADE)
    reply_to = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='reply',on_delete=models.CASCADE,null=True)
    parent = models.ForeignKey('self',related_name='parent_comment',on_delete=models.CASCADE,null=True)
    root = models.ForeignKey('self',related_name='root_comment',on_delete=models.CASCADE,null=True)
    commentTime = models.DateTimeField(auto_now_add=True)
    commentText = models.TextField()

    class Meta:
        ordering = ['-commentTime']

    def __str__(self):
        return self.commentText



