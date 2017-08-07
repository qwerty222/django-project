# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.http import HttpResponse
from django.core.paginator import Paginator, Page, EmptyPage
from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm


def paginate(request, qs, url):
    limit = 10    
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(qs, limit)
    paginator.baseurl = url + '/?page='
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return paginator, page

def test(request, *args, **kwargs):
    return HttpResponse('OK')

@require_GET # /?page=2
def new_questions(request):
    questions_query_set = Question.objects.new()
    paginator, page = paginate(request, questions_query_set, '')
    return render(request, 'questions.html', {
        'questions': page.object_list,
        'paginator': paginator, 'page': page,
    })

@require_GET # /popular/?page=3
def popular_questions(request):
    popular_query_set = Question.objects.popular()
    paginator, page = paginate(request, popular_query_set, '/popular')
    return render(request, 'questions.html', {
        'questions': page.object_list,
        'paginator': paginator, 'page': page,
    })

# /question/id/
def question_answers(request, id):
    question = get_object_or_404(Question, id=id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save()
            url = answer.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm()
    return render(request, 'question_answers.html', {'question':question, 'form': form})

# /ask/
def question_add(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'question_add.html', {'form': form})






