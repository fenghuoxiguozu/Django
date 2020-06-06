from django import forms
from django.core.cache import cache
from account.models import SEX_CHOICE
from django.contrib.auth import authenticate,get_user_model
User = get_user_model()


class LoginForm(forms.Form):
    email = forms.CharField(label="邮箱", required=True,
        widget=forms.TextInput(attrs={'class': 'ui left icon input', 'placeholder': '请输入邮箱'}))
    password = forms.CharField(label="密码", min_length=6, max_length=12, required=True,
       error_messages={"min_length": "最小长度为6位", "max_length": "最大长度为12位",'required': '密码输入格式有误'},
       widget=forms.PasswordInput(attrs={'class': 'ui left icon input', 'placeholder': '请输入密码'}))
    remember = forms.BooleanField(label="记住我", required=False)
    captcha = forms.CharField(label="图形验证码", max_length=4, required=True,
                              widget=forms.TextInput(attrs={'placeholder': '请输入验证码'}))


    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        user = authenticate(email=email, password=password)
        if user is None:
            raise forms.ValidationError('用户名或密码不正确')
        else:
            self.cleaned_data['user'] = user
        return self.cleaned_data

    def clean_captcha(self):
        captcha = self.cleaned_data.get('captcha')
        cache_captcha = cache.get(captcha.lower())
        if not cache_captcha or cache_captcha.lower() != captcha.lower():
            raise forms.ValidationError("图形验证码错误")


class RegisterForm(forms.Form):
    email = forms.CharField(label="邮箱", required=True,
        widget=forms.TextInput(attrs={'class': 'ui left icon input', 'placeholder': '请输入邮箱'}))
    password = forms.CharField(label="密码",min_length=6,max_length=12,required=True,
       error_messages={"min_length":"最小长度为6位","max_length":"最大长度为12位",'required':'密码输入格式有误'},
       widget=forms.PasswordInput(attrs={'class':'ui left icon input','placeholder':'请输入密码'}))
    password_again = forms.CharField(label="确认密码",min_length=6,max_length=12,required=True,
        widget=forms.PasswordInput(attrs={'class':'ui left icon input','placeholder':'请再次输入密码'}),
        error_messages={"min_length":"最小长度为6位","max_length":"最大长度为12位",'required':'密码输入格式有误'})
    captcha = forms.CharField(label="图形验证码",max_length=4,required=True,widget=forms.TextInput(attrs={'placeholder':'请输入验证码'}))
    code = forms.CharField(label="邮箱验证码", max_length=4, required=True,widget=forms.TextInput(attrs={'placeholder': '请输入邮箱验证码'}))

    def __init__(self, *args, **kwargs):
        if 'request' in kwargs:
            self.request = kwargs.pop('request')
        super(RegisterForm, self).__init__(*args, **kwargs)

    def clean(self):
        email_code = self.request.session.get('email_code','')
        input_code = self.cleaned_data.get('code','')
        if input_code=='' or email_code != input_code:
            raise forms.ValidationError("邮箱验证码错误")
        return self.cleaned_data

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("该用户已被注册")
        return email

    def clean_password_again(self):
        password = self.cleaned_data['password']
        password_again = self.cleaned_data['password_again']
        if password != password_again:
            raise forms.ValidationError("两次输入的密码不一致")
        return password_again

    def clean_captcha(self):
        captcha = self.cleaned_data.get('captcha')
        cache_captcha = cache.get(captcha.lower())
        if not cache_captcha or cache_captcha.lower() != captcha.lower():
            raise forms.ValidationError("图形验证码错误")


class NicknameForm(forms.Form):
    nickname_new = forms.CharField(label="昵称", required=True)

class SexForm(forms.Form):
    sex = forms.ChoiceField(label="性别", choices=SEX_CHOICE,required=True,widget=forms.Select)

class HeadForm(forms.Form):
    head = forms.ImageField(label="头像",required=True,widget=forms.FileInput)