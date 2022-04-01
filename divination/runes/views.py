import random

from django.shortcuts import render
from django.http import Http404
from django.utils.translation import gettext as _

from runes.models import Divination, Question, Rune
from runes.forms import QuestionForm


def one_rune_divination_question(request, divination_id):
    divination = Divination.objects.get(id=divination_id)

    form = QuestionForm()

    return render(request, 'runes/rune_divination.html', {
        'divination': divination,
        'form': form,
        'divination_id': divination_id,
    })


def divination_answer(request, divination_id):
    question = request.POST['question']
    referer = request.headers.get('Referer', '')
    origin = request.headers.get('Origin', '')

    if divination_id == 1:
        answer, forecast_type = one_rune_divination_answer(request)
    elif divination_id == 2:
        pass
    elif divination_id == 3:
        pass
    else:
        raise Http404(_('Forecast not found'))

    question = Question(question=question, referer=referer, origin=origin)
    # question.answer = {
    #     'forecast_type': forecast_type,
    #     'rune': answer['rune'].title,
    #     'is_inverted': answer['is_inverted_str'],
    # }

    question.save()

    return render(request, 'runes/answer.html', {
        'answers': answer,
        'forecast_type': forecast_type
    })


def one_rune_divination_answer(request):
    random.seed()
    locale = 'ru_ua'

    forecast_type = 'Гадание на одной руне'
    rune_order = random.randint(1, 24)
    rune = Rune.objects.get(order=rune_order)

    translation = rune.runetranslation_set.get(locale=locale)
    forecast = translation.forecast_meaning_direct
    is_inverted_str = 'Прямое положение'
    is_inverted = 0
    if rune.has_inverted:
        is_inverted = random.randint(0, 1)
        if is_inverted == 1:
            is_inverted_str = 'Перевернутое положение'
            forecast = translation.forecast_meaning_inverted

    answer = [{
        'rune': rune,
        'title': translation.title,
        'description': translation.description,
        'is_inverted_str': is_inverted_str,
        'forecast': forecast,
    }]

    return answer, forecast_type
