from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    nickname = models.CharField(max_length=10,default='游客')

    class Meta(AbstractUser.Meta):
        pass
