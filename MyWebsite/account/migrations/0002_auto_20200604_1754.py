# Generated by Django 2.2.1 on 2020-06-04 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=80, verbose_name='密码'),
        ),
    ]
