from django import forms
from users.models import User
from django.forms.models import ModelForm


class loginForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name','last_name')




