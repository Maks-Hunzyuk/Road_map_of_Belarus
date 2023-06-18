from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Cities, Events, Routers, Comment


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError("Password don't match")
        return cd['password2']
    

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class CommentForm(forms.Form):    
    class Meta:
        model = Comment
        fields = ('name', 'body')
        widgets = {
            'name': forms.TextInput(),
            'body' : forms.TextInput()
        }
 


