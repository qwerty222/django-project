# -*- coding: utf-8 -*-
from django import forms
from qa.models import Question, Answer
from django.contrib.auth.models import User


def is_spam(data):
    return False


# - форма добавления вопроса
class AskForm(forms.Form):
    # - поле заголовка    
    title = forms.CharField(max_length=100)
    # - поле текста вопроса
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        if is_spam(self.cleaned_data):
            raise forms.ValidationError(u'Сообщение похоже на спам', code='spam')

    def save(self):
        obj = Question.objects.create(**self.cleaned_data)
        obj.author = self._user
        obj.save()
        return obj


# - форма добавления ответа
class AnswerForm(forms.Form):
    # - поле текста ответа    
    text = forms.CharField(max_length=100)
    # - поле для связи с вопросом
    question = forms.IntegerField()

    def clean(self):
        if is_spam(self.cleaned_data):
            raise forms.ValidationError(u'Сообщение похоже на спам', code='spam')

    def save(self):
        obj = Answer.objects.create(**self.cleaned_data)
        obj.author = self._user
        obj.save()
        return obj


# - форма регистрации нового пользователя
class UserForm(forms.Form):
    # - имя пользователя, логин
    username = forms.CharField(max_length=100)
    # - email пользователя
    email = forms.EmailField()
    # - пароль пользователя
    password = forms.CharField(widget=forms.PasswordInput)  # class Meta: model = User

    def save(self):
        return User.objects.create(**self.cleaned_data)  # create_user('john', 'lennon@thebeatles.com', 'johnpassword')


# - форма логина
class LoginForm(forms.Form):
    # - имя пользователя, логин
    username = forms.CharField(max_length=100)
    # - пароль пользователя
    password = forms.CharField(widget=forms.PasswordInput)

