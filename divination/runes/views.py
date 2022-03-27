import random

from django.shortcuts import render

from runes.models import Divination, Question, Rune
from runes.forms import QuestionForm


def one_rune_divination_question(request, divination_id):
    divination = Divination.objects.get(id=divination_id)

    form = QuestionForm()

    return render(request, 'runes/rune_divination.html', {
        'divination': divination,
        'form': form,
    })


def divination_answer(request):
    question = request.POST['question']
    referer = request.headers.get('Referer', '')
    origin = request.headers.get('Origin', '')

    answer, forecast_type = one_rune_divination_answer(
        request)

    question = Question(question=question, referer=referer, origin=origin)
    question.answer = {
        'forecast_type': forecast_type,
        'rune': answer['rune'].title,
        'is_inverted': answer['is_inverted_str'],
    }
    question.save()

    return render(request, 'runes/answer.html', {
        'answer': answer,
        'forecast_type': forecast_type
    })


def one_rune_divination_answer(request):
    random.seed()

    forecast_type = 'Гадание на одной руне'
    rune_order = random.randint(1, 5)
    rune = Rune.objects.get(order=rune_order)

    forecast = rune.forecast_meaning_direct
    is_inverted_str = 'Прямое положение'
    is_inverted = 0
    if rune.has_inverted:
        is_inverted = random.randint(0, 1)
        if is_inverted == 1:
            is_inverted_str = 'Перевернутое положение'
            forecast = rune.forecast_meaning_inverted

    answer = {
        'rune': rune,
        'is_inverted_str': is_inverted_str,
        'forecast': forecast,
    }

    return answer, forecast_type
