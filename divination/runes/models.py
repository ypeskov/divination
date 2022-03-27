from ipaddress import ip_address
from django.db import models


class Divination(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(unique=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.title}'


class Rune(models.Model):
    order = models.PositiveIntegerField(unique=True)
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    forecast_meaning_direct = models.TextField(blank=True)
    forecast_meaning_inverted = models.TextField(blank=True)
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

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.ip_address} {self.created_at}'
