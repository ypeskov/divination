from django.contrib import admin

from runes.models import Divination, Rune, Question, RuneTranslation


# admin.site.register(Author, AuthorAdmin)
@admin.register(Divination)
class DivinationAdmin(admin.ModelAdmin):
    list_display = ('order', 'title', 'description')
    ordering = ('order',)


@admin.register(RuneTranslation)
class RuneTranslationAdmin(admin.ModelAdmin):
    pass

class RuneTranslationInLine(admin.TabularInline):
  model = RuneTranslation
  extra = 0

@admin.register(Rune)
class RuneAdmin(admin.ModelAdmin):
    list_display = ('order', 'runetranslation_display')
    ordering = ('order',)

    inlines = [RuneTranslationInLine]

    def runetranslation_display(self, obj):
        return ", ".join([
            f"{rt.title} - {rt.locale} " for rt in obj.runetranslation_set.all()
        ])
    runetranslation_display.short_description = "Translations"

    class Media:
        css = {
            'all': ('runes/css/admin.css',)
        }

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass
