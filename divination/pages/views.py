from django.shortcuts import render

from runes.models import Divination


def index(request):
    divinations = Divination.objects.all()

    return render(request, 'pages/main.html', {
        'divinations': divinations
    })
