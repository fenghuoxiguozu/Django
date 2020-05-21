from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from read.models import ReadNumMethod,ReadDetail
from django.contrib.contenttypes.fields import GenericRelation

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
    read_details = GenericRelation(ReadDetail)

    class Meta:
        db_table = 'Article'
        verbose_name = '文章详情'
        verbose_name_plural = '文章详情'

    def __str__(self):
        return self.title




