from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class RegForm(UserCreationForm):
    username= forms.CharField(label=('Username'))
    email= forms.EmailField(label=('Email'),widget=forms.EmailInput())
    password1= forms.CharField(label=('Password'),widget=forms.PasswordInput(attrs={'class':'form-control-warning'}))
    password2= forms.CharField(label=('Confirm Password'),widget=forms.PasswordInput())



    class Meta:
        model= User
        fields=['username', 'email', 'password1','password2']
