from django import forms

class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label='Введите логин')
    password = forms.CharField(min_length=8, label='Введите пароль')
    repeat_password = forms.CharField(min_length=8, label='Повторите пароль')
    age = forms.CharField(max_length=3, label='Введите свой возраст')

class UserLogIn(forms.Form):
    username = forms.CharField(max_length=30, label='Введите логин')
    password = forms.CharField(min_length=8, label='Введите пароль')

class CreateBook(forms.Form):
    title = forms.CharField(max_length=50)
    author = forms.CharField(max_length=50)
    description = forms.CharField(max_length=3000)
    genre = forms.CharField(max_length=15)