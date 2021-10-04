from django import forms
from home.models import UserInfo

class PostForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields ='__all__'