import xadmin
from .models import *


class CommentAdmin():
    list_display = ['user','commentTime','object_id','commentText','parent','root']




xadmin.site.register(Comment,CommentAdmin)
