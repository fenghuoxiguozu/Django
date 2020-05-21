import xadmin
from .models import *


class ReadNumAdmin():
    list_display = ['read_num','content_type','object_id',]


class ReadDetailAdmin():
    list_display = ['read_num','read_date','content_type','object_id',]

xadmin.site.register(ReadNum,ReadNumAdmin)
xadmin.site.register(ReadDetail,ReadDetailAdmin)


# Register your models here.
