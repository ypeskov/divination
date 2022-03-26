from django.shortcuts import render

from runes.models import Rune

def rune_divination(request, divination_id):
    divination = Rune.objects.filter(id=divination_id)
    print(divination)
    return render(request, 'runes/rune_divination.html', {
        'divination': {'title': 'LALALALA'}
    })
