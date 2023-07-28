from django import forms

class Search(forms.Form):
    input = forms.CharField(required=False, max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Поиск'}))