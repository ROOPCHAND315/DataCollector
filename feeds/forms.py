from django import forms

class FeedForm(forms.Form):
    domain = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control mr-2', 'placeholder': 'Search'}))
    


