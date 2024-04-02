from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Acrescenta novos campos ao formulário de cadastro de usuários
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']