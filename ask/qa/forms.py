from django import forms
from qa.models import Question, Answer


def is_spam(data):
    return False

# - форма добавления вопроса
class AskForm(forms.Form):
    # - поле заголовка    
    title = forms.CharField(max_length=100)
    # - поле текста вопроса
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        if is_spam(self.clean_data):
            raise forms.ValidationError(u'Сообщение похоже на спам', code='spam')

    def save(self):
        return Question.objects.create(**self.cleaned_data)

# - форма добавления ответа
class AnswerForm(forms.Form):
    # - поле текста ответа    
    text = forms.CharField(max_length=100)
    # - поле для связи с вопросом
    question = forms.CharField(max_length=100)

    def clean(self):
        if is_spam(self.clean_data):
            raise forms.ValidationError(u'Сообщение похоже на спам', code='spam')

    def save(self):
        return Answer.objects.create(**self.cleaned_data)

