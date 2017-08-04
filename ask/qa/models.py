# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# - менеджер модели Question
class QuestionManager(models.):
# - метод возвращающий последние добавленные вопросы
    def new():
        #return Question.objects.order_by('-added_at')[:5]
        pass
# - метод возвращающий вопросы отсортированные по рейтингу
    def popular():
        #return Question.objects.order_by('-rating')
        pass


# - вопрос
class Question(models.Model):
# - заголовок вопроса
    title = models.CharField(max_length=255)
# - полный текст вопроса
    text = models.TextField()
# - дата добавления вопроса
    added_at = models.DateField(blank = True, auto_now_add=True)
# - рейтинг вопроса (число)
    rating = models.IntegerField(default=0)
# - автор вопроса
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='question_author_1')
# - список пользователей, поставивших "лайк"
    likes = models.ManyToManyField(User, related_name='question_like_author')


# - ответ
class Answer(models.Model):
# - текст ответа
    text = models.TextField()
# - дата добавления ответа
    added_at = models.DateField()
# - вопрос, к которому относится ответ
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
# - автор ответа
    author = models.ForeignKey(User, on_delete=models.CASCADE)
