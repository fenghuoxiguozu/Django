import xadmin
from .models import *


class CommentAdmin():
    list_display = ['user','commentTime','content_type','object_id','commentText',]




xadmin.site.register(Comment,CommentAdmin)
