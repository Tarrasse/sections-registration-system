from django import forms
from django.core import validators


class login_form(forms.Form):
    id = forms.IntegerField()
    password = forms.CharField(max_length=255)


class sign_up_form(forms.Form):
    id = forms.IntegerField()
    name = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)
    password2 = forms.CharField(max_length=255)
