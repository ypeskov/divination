from django.urls import path

from . import views

urlpatterns = [
    path('<int:divination_id>', views.one_rune_divination_question),
    path('answer/', views.divination_answer),
]
