from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Zadej URL písničky:', max_length=1000)