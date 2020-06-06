from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from read.models import ReadNumMethod,ReadDetail
from django.contrib.contenttypes.fields import GenericRelation
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=15)

    class Meta:
        db_table = 'ArticleTag'
        verbose_name = '文章标签'
        verbose_name_plural = '文章标签'

    def __str__(self):
        return self.name


class Article(models.Model,ReadNumMethod):
    title = models.CharField(max_length=100)
    content = RichTextUploadingField()
    published = models.DateField(auto_now_add=True)
    tagName = models.ManyToManyField('Tag')
    photo = ProcessedImageField(  # 注意：ImageSpecField 不会生成数据库表的字段
        upload_to='article/%Y/%m',
        processors=[ResizeToFill(180, 140)],  # 处理成一寸照片的大小
        format='JPEG',  # 处理后的图片格式
        options={'quality': 95},  # 处理后的图片质量
        default='article/default/photo_1.jpg'
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    read_details = GenericRelation(ReadDetail)

    class Meta:
        db_table = 'Article'
        verbose_name = 'Article'
        verbose_name_plural = '文章详情'

    def __str__(self):
        return self.title




