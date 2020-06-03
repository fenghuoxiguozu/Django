"""
Django settings for MyWebsite project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os,sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4#=t$*8n)9ia9f(l_!yd*xs$3os=p3_1(%drz8rt0m^!(l1$rx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'xadmin',
    'crispy_forms',
    'ckeditor',
    'ckeditor_uploader',
    'article',
    'read',
    'comment',
    'like',
    'account',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MyWebsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries': {
                'comment_tags': 'comment.template_tags.comment_tags'
                # 'like_tags': 'like.template_tags.like_tags'

            },
        },

    },
]

WSGI_APPLICATION = 'MyWebsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'wordpress', # 数据库名
        'USER': 'root', # 账号
        'PASSWORD': 'lub08753', # 密码
        'HOST': 'localhost', # HOST
        'POST': 3306, # 端口
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static'),]
sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))

# meida
MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')

# 配置ckeditor
CKEDITOR_UPLOAD_PATH='upload/'
EACH_PAGE_BLOGS_NUMBER=7
CKEDITOR_CONFIGS={
    'default':{},
    'comment_ckeditor':{
        # 使用简体中文
        'language':'zh-cn',
        # 编辑器的宽高请根据你的页面自行设置
        'width':'600px',
        'height':'200px',
        'image_previewText':' ',
        'tabSpaces': 4,
        'toolbar': 'Custom',
        # 添加按钮在这里
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline', 'Format', 'RemoveFormat','Blockquote'],
            ['TextColor', 'BGColor'],
            ['NumberedList', 'BulletedList'],
            ['Smiley', 'SpecialChar','Blockquote', 'CodeSnippet'],
            # ['Image', 'Link', 'Unlink'],
            ['Maximize']
        ],
            # 加入代码块插件
        # 'extraPlugins': ','.join(['codesnippet']),
        'removePlugins':'elementspath',
        'resize_enable':False,
    }
}




CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'my_cache_table', # 数据库表
    }
}
# python manage.py createcachetable

AUTH_USER_MODEL = 'account.User'

# send e-mail
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  #email后端
EMAIL_USE_TLS = False   #是否使用TLS安全传输协议 端口25
EMAIL_USE_SSL = True    #是否使用SSL加密，qq企业邮箱要求使用 端口465
EMAIL_HOST = 'smtp.qq.com'   #发送邮件的邮箱 的 SMTP服务器，这里用了qq企业邮箱
EMAIL_PORT = 465     #发件箱的SMTP服务器端口
EMAIL_HOST_USER = '1058247664@qq.com'    #发送邮件的邮箱地址
EMAIL_HOST_PASSWORD = 'fiegbbvupwwxbedd'         #发送邮件的邮箱密码