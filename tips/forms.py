from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm




class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        
    class Meta:
        model = User 
        fields = ("username", "password1", "password2",)
        


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        
from django import forms
from . models import Topic, Comment



#スレッド作成フォーム
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ('user', 'title')
        labels = {
            'user': 'ユーザー',
            'title': 'スレッド名'
        }
        
#コメント作成フォーム
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user', 'comment', 'img')
        labels = {
            'user': 'ユーザー',
            'comment': 'コメント',
            'img': '画像'
        }