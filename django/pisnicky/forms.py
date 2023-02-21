from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Zadej URL písničky:', max_length=1000)

class SongNameForm(forms.Form):
    songName = forms.CharField(label='Název písničky:', max_length=1000)
    author = forms.CharField(label='Jméno autora:', max_length=1000)