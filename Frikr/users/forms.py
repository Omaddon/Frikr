# -*- coding: utf-8 -*-

from django import forms


class LoginForm(forms.Form):

    usr = forms.CharField(label="User Name")
    pwd = forms.CharField(label="Password", widget=forms.PasswordInput())
