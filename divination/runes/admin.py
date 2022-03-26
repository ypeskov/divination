from django.contrib import admin

from runes.models import Divination


# admin.site.register(Author, AuthorAdmin)
@admin.register(Divination)
class DivinationAdmin(admin.ModelAdmin):
    list_display = ('order', 'title', 'description')
    ordering = ('order',)
