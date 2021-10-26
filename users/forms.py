from django import forms
from django.contrib.auth.models import User


class LoginForms(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'password')


class RegisterForms(forms.ModelForm):
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'last_name', 'email', 'password')
