from django import forms
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Search(forms.Form):
    input = forms.CharField(required=False, max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Поиск'}))

class PostEdit(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title_image', 'title', 'main_text', 'image', 'image1', 'image2', 'text', 'file']
class UserReg(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']