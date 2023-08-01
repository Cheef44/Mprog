from django import forms
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Search(forms.Form):
    input = forms.CharField(required=False, max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Поиск'}))

class PostEdit(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title_image', 'title', 'main_text', 'image', 'text', 'file']