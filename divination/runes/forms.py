from django import forms


class QuestionForm(forms.Form):
    question = forms.CharField(
        max_length=300, label='Ваш вопрос', initial='', required=False)
