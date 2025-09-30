from django.contrib import admin

from dict.models import Language, Meaning, Word


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Meaning)
class MeaningAdmin(admin.ModelAdmin):
    list_display = ['meaning']


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ['title']
