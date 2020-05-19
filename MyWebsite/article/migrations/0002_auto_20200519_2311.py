# Generated by Django 2.2.1 on 2020-05-19 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '文章详情', 'verbose_name_plural': '文章详情'},
        ),
        migrations.CreateModel(
            name='ReadNum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read_num', models.IntegerField(default=0)),
                ('article', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='article.Article')),
            ],
            options={
                'verbose_name': '文章阅读量',
                'verbose_name_plural': '文章阅读量',
                'db_table': 'ReadNum',
            },
        ),
    ]