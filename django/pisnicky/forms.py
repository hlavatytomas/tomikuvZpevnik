from django import forms
from django.utils.safestring import mark_safe

class NameForm(forms.Form):
    your_name = forms.CharField(label='Zadej URL písničky, nebo nechej prázdné:', required=False, max_length=1000)

class SongNameForm(forms.Form):
    # songName = forms.CharField(label='Název písničky:', max_length=1000)
    name = forms.CharField(
        label='Název písničky',
        widget=forms.TextInput(
        attrs={
            # 'placeholder': 'Name', 
            'class': 'name_field', 
            # 'class': 'form-control'
        }))
    author = forms.CharField(label=mark_safe('Autor/Interpret'), max_length=1000)
    capo = forms.IntegerField(label=mark_safe('Capo:'),  required=False)
    owner = forms.CharField(label=mark_safe('Přidal (T H K L Y):'), max_length=1000)
    text = forms.CharField(
        label=mark_safe('Text písně:'),widget=forms.Textarea()
    )