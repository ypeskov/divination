from django.contrib import admin

from runes.models import Divination


class AuthorAdmin(admin.ModelAdmin):
    admin.site.register(Divination)
