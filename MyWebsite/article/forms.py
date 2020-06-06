from django import forms
from django.contrib.contenttypes.models import ContentType
from django.db.models import ObjectDoesNotExist
from ckeditor.widgets import CKEditorWidget
from comment.models import Comment
from article.models import Tag

class CommentForm(forms.Form):
    content_type = forms.CharField(widget=forms.HiddenInput)
    object_id = forms.IntegerField(widget=forms.HiddenInput)
    commentText = forms.CharField(widget=CKEditorWidget(config_name='comment_ckeditor'),
                                  error_messages={"required":"评论内容不为空"})
    reply_id = forms.IntegerField(widget=forms.HiddenInput(attrs={"id":"reply_id"}))



    def __init__(self,*args,**kwargs):
        if 'user' in kwargs:
            self.user = kwargs.pop('user')
        super(CommentForm,self).__init__(*args,**kwargs)

    def clean(self):
        if self.user.is_authenticated:
            self.cleaned_data['user'] = self.user
        else:
            raise forms.ValidationError('用户未登陆')

        content_type = self.cleaned_data['content_type']
        object_id = self.cleaned_data['object_id']
        try:
            model_class1 = ContentType.objects.get(model=content_type)
            model_class = model_class1.model_class()
            model_object = model_class.objects.get(pk=object_id)
        except ObjectDoesNotExist:
            raise forms.ValidationError("评论对象不存在")
        self.cleaned_data['content_object'] = model_object
        return self.cleaned_data

    def clean_reply_id(self):
        reply_id = self.cleaned_data['reply_id']
        if reply_id == 0:
            self.cleaned_data['parent'] = None
        elif Comment.objects.filter(pk=reply_id).exists():
            self.cleaned_data['parent'] = Comment.objects.get(pk=reply_id)
        else:
            raise forms.ValidationError('回复出错')
        return reply_id


class ArticleForm(forms.Form):
    all_tags = Tag.objects.all().values('id','name')
    tag_list=[]
    for tag in all_tags:
        tag_list.append([tag['id'],tag['name']])
    input_style = 'width:518px;height:50px;background: #f6f6f6;border: 1px solid #6E6E6E;color: #202124;border-radius: 5px;'
    file_style = 'color: red;'
    title = forms.CharField(required=True,max_length=100,widget=forms.TextInput(
        attrs={'placeholder':'请输入文章标题','class':'ui input error','style':input_style}))
    content = forms.CharField(required=True,widget=CKEditorWidget(
        attrs={'placeholder':'请输入正文'},config_name='comment_ckeditor'),error_messages={"required":"文章内容不为空"})
    tagName = forms.MultipleChoiceField(choices=tag_list,widget=forms.SelectMultiple(
        attrs={'class':'ui dropdown','placeholder':'请输入文章标签，可多选'}))
    photo = forms.ImageField(label="文章正文图像", widget=forms.FileInput(attrs={'style':file_style}))

