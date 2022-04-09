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
    title = models.CharField(max_length=50)
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
    answer = models.JSONField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.origin} {self.created_at}'


class RuneTranslation(models.Model):
    locale = models.CharField(max_length=20)
    title = models.CharField(blank=True, max_length=100)
    description = HTMLField(blank=True)
    forecast_meaning_direct = HTMLField(blank=True)
    forecast_meaning_inverted = HTMLField(blank=True)

    rune = models.ForeignKey(Rune, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'Rune: {self.title}, Locale: {self.locale}'
