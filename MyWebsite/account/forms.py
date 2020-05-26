from django import forms
from django.contrib.auth import authenticate,get_user_model
User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(label="用户名",required=True,widget=forms.TextInput(attrs={'class':'ui left icon input','placeholder':'请输入用户名'}))
    password = forms.CharField(label="密码",widget=forms.PasswordInput(attrs={'class':'ui left icon input','placeholder':'请输入密码'}))

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError('用户名或密码不正确')
        else:
            self.cleaned_data['user'] = user
        return self.cleaned_data


class RegisterForm(forms.Form):
    username = forms.CharField(label="用户名",required=True,min_length=6,max_length=12,
       widget=forms.TextInput(attrs={'class':'ui left icon input','placeholder':'请输入用户名'}))
    email = forms.EmailField(label="邮箱",required=True,widget=forms.EmailInput(
        attrs={'class':'ui left icon input','placeholder':'请输入邮箱'}))
    password = forms.CharField(label="密码",min_length=6,max_length=12,widget=forms.PasswordInput(
        attrs={'class':'ui left icon input','placeholder':'请输入密码'}))
    password_again = forms.CharField(label="确认密码",min_length=6,max_length=12,widget=forms.PasswordInput(
        attrs={'class':'ui left icon input','placeholder':'请再次输入密码'}))


    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("该用户已被注册")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("该邮箱已被注册")
        return email

    def clean_password_again(self):
        password = self.cleaned_data['password']
        password_again = self.cleaned_data['password_again']
        if password != password_again:
            raise forms.ValidationError("两次输入的密码不一致")
        return password_again


class NicknameForm(forms.Form):
    nickname_new = forms.CharField(label="昵称",required=True,
       widget=forms.TextInput(attrs={'placeholder':'请输入新昵称'}))

    def clean_nickname_new(self):
        nickname_new = self.cleaned_data.get('nickname_new','').strip()
        if nickname_new == '':
            raise forms.ValidationError('内容不能为空')
        return nickname_new


class EmailForm(forms.Form):
    email = forms.EmailField(label="邮箱",required=True,
       widget=forms.EmailInput(attrs={'placeholder':'请输入邮箱'}))
    verify_code = forms.CharField(label="",required=True,
      widget=forms.TextInput(attrs={"placeholder":"点击发送验证码"}))