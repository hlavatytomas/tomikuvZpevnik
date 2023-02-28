from django import forms
from django.utils.safestring import mark_safe

class NameForm(forms.Form):
    your_name = forms.CharField(label='Zadej URL písničky:', max_length=1000)

class SongNameForm(forms.Form):
    # songName = forms.CharField(label='Název písničky:', max_length=1000)
    name = forms.CharField(
        label='Název písničky',
        widget=forms.TextInput(
        attrs={
            'placeholder': 'Name', 
            'style': 'width: 400px;', 
            # 'class': 'form-control'
        }))
    author = forms.CharField(label=mark_safe('<br><br>Autor/Interpret'), max_length=1000)
    capo = forms.CharField(label=mark_safe('<br><br>Capo:'), max_length=1000, required=False)
    owner = forms.CharField(label=mark_safe('<br><br>Přidal:'), max_length=1000)