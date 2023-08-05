from django import forms
from .models import Post
from .models import PostImage

class Search(forms.Form):
    input = forms.CharField(required=False, max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Поиск'}))

class PostEdit(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title_image', 'title', 'main_text', 'text', 'file']

class PostImageDawnlod(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'multiple': True}),
        }