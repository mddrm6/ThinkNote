from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs= {
        'placeholder': 'Your username',
        'class': 'signup__input',
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs= {
        'placeholder': 'Your password',
        'class': 'signup__input',
    }))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs= {
        'placeholder': 'Your username',
        'class': 'signup__input',
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs= {
        'placeholder': 'Your email address',
        'class': 'signup__input',
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs= {
        'placeholder': 'Your password',
        'class': 'signup__input',
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs= {
        'placeholder': 'Repeat password',
        'class': 'signup__input',
    }))