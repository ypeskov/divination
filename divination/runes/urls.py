from django.urls import path

from . import views

app_name = 'runes'

urlpatterns = [
    path('<int:divination_id>', views.forecast_question, name='forecast_question'),
    path('answer/<int:divination_id>', views.divination_answer, name='forecast_answer'),
]
