from django.urls import path

from . import views

urlpatterns = [
    path('<int:divination_id>', views.rune_divination),
]
