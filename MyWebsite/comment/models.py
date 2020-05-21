from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User
# Create your models here.

class Comment(models.Model):
    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type','object_id')

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    commentTime = models.DateTimeField(auto_now_add=True)
    commentText = models.TextField()

    class Meta:
        ordering = ['-commentTime']



