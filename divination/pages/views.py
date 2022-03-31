from django.shortcuts import render
from django.utils.translation import gettext as _

from runes.models import Divination


def index(request):
    divinations = Divination.objects.all()

    return render(request, 'pages/main.html', {
        'divinations': divinations
    })
