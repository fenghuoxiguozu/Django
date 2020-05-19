from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=15)

    class Meta:
        db_table = 'ArticleTag'
        verbose_name = '文章标签'
        verbose_name_plural = '文章标签'

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextUploadingField()
    published = models.DateField(auto_now_add=True)
    tagName = models.ManyToManyField('Tag')

    class Meta:
        db_table = 'Article'
        verbose_name = '文章详情'
        verbose_name_plural = '文章详情'

    def __str__(self):
        return self.title


class ReadNum(models.Model):
    read_num = models.IntegerField(default=0)
    article = models.OneToOneField(Article,on_delete=models.CASCADE)

    class Meta:
        db_table = 'ReadNum'
        verbose_name = '文章阅读量'
        verbose_name_plural = '文章阅读量'