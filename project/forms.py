from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import TextInput, PasswordInput

from project.models import Category


class CategoryForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=100,
                           required=True, label='Название',
                           widget=TextInput(
                               attrs={
                                   'placeholder': 'Название категории'
                               }
                           ))

    def clean_name(self):
        name = self.cleaned_data['name']
        print(name)
        categories = Category.objects.filter(name=name)
        print(categories.count())
        if categories.count() > 0:
            raise ValidationError('Такая категория уже существует')
        return name

    def save(self, commit=True):
        category = Category.objects.create(name=self.cleaned_data['name'])
        category.save()
        return category


class UserCreationForm(forms.Form):
    username = forms.CharField(max_length=100,
                               widget=TextInput(attrs={
                                   'placeholder': 'UserName',
                                   'class': 'form-control'
                               }))
    password = forms.CharField(max_length=100,
                               widget=PasswordInput(attrs={
                                   'placeholder': 'Password',
                                   'class': 'form-control'
                               }))

    password1 = forms.CharField(max_length=100,
                                widget=PasswordInput(attrs={
                                    'placeholder': 'Repeat Password',
                                    'class': 'form-control'
                                }))

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).count() > 0:
            raise ValidationError('Такой пользователь уже существует!')
        return username

    def clean_password1(self):
        if self.cleaned_data['password'] != self.cleaned_data['password1']:
            raise ValidationError('Пароли не совпададают!')
        return self.cleaned_data['password1']

    def save(self):
        user = User.objects.create_user(username=self.cleaned_data['username'],
                                        email='osymbat1@gmail.com',
                                        password=self.cleaned_data['password1'])
        user.save()
        return user
