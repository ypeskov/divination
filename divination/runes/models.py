from django.db import models

from tinymce.models import HTMLField


class Divination(models.Model):
    title = models.CharField(max_length=100)
    order = models.PositiveIntegerField(unique=True, null=True)
    description = HTMLField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.title}'


class Rune(models.Model):
    order = models.PositiveIntegerField(unique=True)
    title = models.CharField(max_length=30)
    description = HTMLField(blank=True)
    forecast_meaning_direct = HTMLField(blank=True)
    forecast_meaning_inverted = HTMLField(blank=True)
    has_inverted = models.BooleanField()
    img_direct = models.URLField(null=True, blank=True)
    img_inverted = models.URLField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.title}'

class Question(models.Model):
    question = models.CharField(max_length=300, null=True, blank=True)
    referer = models.CharField(null=True, max_length=100)
    origin = models.CharField(null=True,max_length=100)
    answer = models.JSONField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.origin} {self.created_at}'
