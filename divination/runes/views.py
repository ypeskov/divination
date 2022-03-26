from django.shortcuts import render

from runes.models import Divination

def rune_divination(request, divination_id):
    divination = Divination.objects.get(id=divination_id)

    return render(request, 'runes/rune_divination.html', {
        'divination': divination
    })
