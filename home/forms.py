from django import forms
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    email = forms.EmailField(required=True, label="", widget=forms.TextInput(attrs={'placeholder':'Email'}))
    username = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password1 = forms.CharField(
        required = True,
        label = "",
        widget = forms.PasswordInput(attrs={'placeholder':'Password'})
    )
    password2 = forms.CharField(
        required = True,
        label = "",
        widget = forms.PasswordInput(attrs={'placeholder':'Password Confirmation'})
    )


    class Meta:
        model = User
        fields = ('email','username','password1','password2')

class UserInfoForm(forms.ModelForm):
    class Meta():
        model = UserInfo
        fields =('full_name','address','country','city','Phone_Number')