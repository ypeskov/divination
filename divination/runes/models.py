from django.db import models


class Divination(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
