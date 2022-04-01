from django.urls import path

from . import views

app_name = 'runes'

urlpatterns = [
    path('<int:divination_id>', views.one_rune_divination_question, name='forecasts_list'),
    path('answer/<int:divination_id>', views.divination_answer, name='forecast_answer'),
]
