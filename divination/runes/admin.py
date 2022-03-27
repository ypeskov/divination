from django.contrib import admin

from runes.models import Divination, Rune, Question


# admin.site.register(Author, AuthorAdmin)
@admin.register(Divination)
class DivinationAdmin(admin.ModelAdmin):
    list_display = ('order', 'title', 'description')
    ordering = ('order',)


@admin.register(Rune)
class RuneAdmin(admin.ModelAdmin):
    list_display = ('order', 'title' )
    ordering = ('order',)

    class Media:
        css = {
            'all': ('runes/admin.css',)
        }

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass
