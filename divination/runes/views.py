import random

from django.shortcuts import render
from django.http import Http404
from django.utils.translation import gettext as _

from runes.models import Divination, Question, Rune
from runes.forms import QuestionForm


def forecast_question(request, divination_id):
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
    forecast_type = _(Divination.objects.get(order=divination_id).title)

    if divination_id == 1:
        answer = provide_rune(1)
    elif divination_id == 2:
        answer = provide_rune(2)
    elif divination_id == 3:
        answer = provide_rune(3)
    else:
        raise Http404(_('Forecast not found'))

    question = Question(question=question, referer=referer, origin=origin)
    question.save()

    template = get_template_name(divination_id)
    return render(request, template, {
        'answers': answer,
        'forecast_type': forecast_type
    })


def get_template_name(divination_id):
    if divination_id == 1:
        template = 'runes/1_rune_answer.html'
    elif divination_id == 2:
        template = 'runes/2_rune_answer.html'
    elif divination_id == 3:
        template = 'runes/3_rune_answer.html'
    else:
        raise Http404()
    return template


def provide_rune(number_of_runes):
    random.seed()
    locale = 'ru_ua'

    # generate all runes orders
    orders = [o for o in range(1, 25)]
    random.shuffle(orders)

    rune_orders = []
    while len(rune_orders) < number_of_runes:
        rune_orders.append(orders.pop())

    runes = Rune.objects.filter(order__in=rune_orders)
    answers = []
    for rune in runes:
        translation = rune.runetranslation_set.get(locale=locale)
        forecast = translation.forecast_meaning_direct
        is_inverted_str = 'Прямое положение'
        if rune.has_inverted:
            is_inverted = random.randint(0, 1)
            if is_inverted == 1:
                is_inverted_str = 'Перевернутое положение'
                forecast = translation.forecast_meaning_inverted

        answers.append({
            'rune': rune,
            'title': translation.title,
            'description': translation.description,
            'is_inverted_str': is_inverted_str,
            'forecast': forecast,
        })

    return answers
