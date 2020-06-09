from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db.models.fields import exceptions
from django.utils import timezone
from django.conf import settings

# Create your models here.
class ReadNum(models.Model):
    read_num = models.IntegerField(default=0)
    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type','object_id')

    class Meta:
        db_table = 'ReadNum'
        verbose_name = '文章阅读量'
        verbose_name_plural = '文章阅读量'


class ReadDetail(models.Model):
    read_num = models.IntegerField(default=0)
    read_date = models.DateField(default=timezone.now)
    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type','object_id')
    # readUser = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    class Meta:
        db_table = 'ReadDetailNum'
        verbose_name = '文章详情阅读量'
        verbose_name_plural = '文章详情阅读量'

class ReadNumMethod():
    def get_read_num(self):
        try:
            ct = ContentType.objects.get_for_model(self)
            read_num = ReadNum.objects.get(content_type=ct,object_id=self.pk)
            return read_num.read_num
        except exceptions.ObjectDoesNotExist:
            return 0
