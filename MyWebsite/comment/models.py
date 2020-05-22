from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User
# Create your models here.

class Comment(models.Model):
    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type','object_id')

    user = models.ForeignKey(User, related_name='comments',on_delete=models.CASCADE)
    reply_to = models.ForeignKey(User,related_name='reply',on_delete=models.CASCADE,null=True)
    parent = models.ForeignKey('self',related_name='parent_comment',on_delete=models.CASCADE,null=True)
    root = models.ForeignKey('self',related_name='root_comment',on_delete=models.CASCADE,null=True)
    commentTime = models.DateTimeField(auto_now_add=True)
    commentText = models.TextField()

    class Meta:
        ordering = ['-commentTime']

    def __str__(self):
        return self.commentText



