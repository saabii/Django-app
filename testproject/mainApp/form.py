from django import forms


class SearchForm(forms.Form):
    q = forms.CharField(widget=forms.TextInput(attrs={
        'size': 30,
        'class': 'form-control search-query',
        'autofocus': 'autofocus',
        'placeholder': 'text'
    }))