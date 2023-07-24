from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from .bulma_mixin import BulmaMixin

class SignInForm(BulmaMixin, AuthenticationForm):
    username = forms.CharField(label='Напишите никнейм')
    # widget=forms.TextInput(attrs={
    #     'class': 'input', 'placeholder': 'Введите никнейм'
    # })
    password = forms.CharField(widget=forms.PasswordInput(),
                               label='Напишите пароль')
    # widget=forms.PasswordInput(
    #     attrs={'class': 'input', 'placeholder': 'Введите пароль'})
    
    class Meta:
        model = User
        fields = ['username', 'password']


class SignUpForm(BulmaMixin, UserCreationForm):
    username = forms.CharField(label='Придумайте никнейм')
    # widget=forms.TextInput(attrs={
    #     'class': 'input', 'placeholder': 'Придумайте никнейм'
    # })
    password1 = forms.CharField(
        widget=forms.PasswordInput(), label='Придумайте пароль')
    # attrs={'class': 'input', 'placeholder': 'Придумайте пароль'}
    password2 = forms.CharField(
        widget=forms.PasswordInput(), label='Повторите пароль')
    attrs={'class': 'input', 'placeholder': 'Повторите пароль'}
    email = forms.CharField(label='Введите адрес почты')
    # widget=forms.EmailInput(
    #     attrs={'class': 'input', 'placeholder': 'Введите адрес почты'})
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class EditProfileForm(BulmaMixin, forms.ModelForm):
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')
    username = forms.CharField(label='Никнейм')
    email = forms.EmailField(label='Адрес почты')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

class ResetPasswordForm(BulmaMixin, PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput, label='Текущий пароль')
    new_password1 = forms.CharField(
        widget=forms.PasswordInput, label='Новый пароль')
    new_password2 = forms.CharField(
        widget=forms.PasswordInput, label='Повторите новый пароль')

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
