from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class BaseRegisterForm(UserCreationForm):
    username = forms.CharField(label='Логин', max_length=64)
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                )
    password2 = forms.CharField(label='Пароль ещё раз',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                )
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")

    class Meta:
        model = User
        fields = ('username',
                  "first_name",
                  "last_name",
                  "email",
                  'password1',
                  'password2',
                  )
