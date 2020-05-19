import xadmin
from .models import *
#配置博客表单显示样式
class ArticleAdmin():
    def all_tags(self, obj):
        return [bt.name for bt in obj.tagName.all()]
    #需要显示的字段
    list_display = ['id','title','published','content','all_tags']
    # 可以用来做搜索条件的字段
    search_fields = ['title',]
    #用时间格式做过滤条件的字段
    list_filter = ['published',]
    #设置可以直接在列表中更改的字段
    # list_editable = ['keywords']


xadmin.site.register(Article,ArticleAdmin)
xadmin.site.register(Tag)
xadmin.site.register(ReadNum)