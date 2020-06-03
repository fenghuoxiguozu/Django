from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from shortuuidfield import ShortUUIDField
from django.contrib.auth.models import PermissionsMixin,BaseUserManager
from django.contrib.auth.base_user import AbstractBaseUser


class UserManager(BaseUserManager):
    def _create_user(self,email,password,**kwargs):
        if not email:
            raise ValueError("必须传入邮箱")
        if not password:
            raise ValueError("必须传入密码")
        user = self.model(email=email,password=password,**kwargs)
        print("save111")
        user.set_password(password)
        print("save112",user)
        print("user pass",user,password)
        user.save()
        print("save113")
        return user

    def create_user(self,email,password,**kwargs):
        kwargs['is_superuser'] = False
        return self._create_user(email=email,password=password,**kwargs)

    def create_superuser(self,email,password,**kwargs):
        kwargs['is_superuser'] = True
        return self._create_user(email=email,password=password,**kwargs)

class User(AbstractBaseUser, PermissionsMixin):
    uid = ShortUUIDField(primary_key=True)
    nickname = models.CharField(max_length=10)
    sex = models.CharField(choices=(('male', '男'),('female', '女'),),default='male',max_length=10)
    email = models.EmailField(verbose_name='邮箱', unique=True)
    phone = models.CharField(verbose_name='手机号', unique=True, max_length=11)
    password = models.CharField(verbose_name='密码', max_length=12)
    data_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(verbose_name='激活状态', default=True)
    is_staff = models.BooleanField(verbose_name='管理员', default=False)
    head = ProcessedImageField(  # 注意：ImageSpecField 不会生成数据库表的字段
        upload_to='user/select',
        processors=[ResizeToFill(80, 80)],  # 处理成一寸照片的大小
        format='JPEG',  # 处理后的图片格式
        options={'quality': 95},  # 处理后的图片质量
        default='user/default/default.jpg'
    )

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    # EMAIL_FIELD = 'email'

    class Meta(AbstractBaseUser.Meta):
        pass