# Generated by Django 2.2.1 on 2020-05-20 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '文章详情', 'verbose_name_plural': '文章详情'},
        ),
    ]