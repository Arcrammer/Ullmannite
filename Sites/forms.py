from django import forms

class SayHelloForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField()
