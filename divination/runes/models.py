from django.db import models


class Divination(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(unique=True, null=True)

    def __str__(self) -> str:
        return f'{self.title}'
