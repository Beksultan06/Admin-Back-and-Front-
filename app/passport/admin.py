from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .translation import *
from .models import *

class PassportAdmin(TranslationAdmin):
    fieldsets = (
        ('Изображения', {
            'fields': ['image'],
        }),
        ('Русская версия', {
            'fields': ['title_ru', 'description_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky', 'description_ky'],
        }),
    )
admin.site.register(Passport, PassportAdmin)



class GeneralInformationImageInline(admin.TabularInline):
    model = GeneralInformationImage
    extra = 1

class GeneralInformationAdmin(TranslationAdmin):

    fieldsets = (
        ('Русская версия', {
            'fields': ['title_ru', 'description_ru'],
        }),
         ('Кыргызская версия', {
            'fields': ['title_ky', 'description_ky'],
        }),

    )
    inlines = [GeneralInformationImageInline]
admin.site.register(GeneralInformation, GeneralInformationAdmin)


class InfoObjectInline(admin.TabularInline):
    model = InfoObject
    extra = 1

    def get_fieldsets(self, request, obj=None):
        fieldsets = (
            ('Russian Version', {
                'fields': ('image',),
            }),
            ('English Version', {
                'fields': ('image',),
            }),
        )
        return fieldsets

class InfoAdmin(TranslationAdmin):
    fieldsets = (
        ('Russian Version', {
            'fields': ('title_ru', 'description_ru',),
        }),
        ('Кыргызская Version', {
            'fields': ('title_ky', 'description_ky',),
        }),
    )
    inlines = [InfoObjectInline]

admin.site.register(Info, InfoAdmin)



class HeadPersonalityAdmin(TranslationAdmin):
    fieldsets = (
        ('Изображение', {
            'fields': ['image_personality',],
        }),
        ('Русская версия', {
            'fields': ['title_personality_ru',],
        }),
        ('Кыргызская версия', {
            'fields': ['title_personality_ky',],
        }),
    )
admin.site.register(HeadPersonality, HeadPersonalityAdmin)



class PersonalityAdmin(TranslationAdmin):
    fieldsets = (
        ('Изображение', {
            'fields': ['image_person',],
        }),
        ('Русская версия', {
            'fields': ['name_person_ru','description_person_ru','all_description_person_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['name_person_ky','description_person_ky','all_description_person_ky'],
        }),
    )
admin.site.register(Personality, PersonalityAdmin)

class HistoryAdmin(TranslationAdmin):
    
    fieldsets = (
        ('Изображения', {
            'fields': ['image'],
        }),
        ('Русская версия', {
            'fields': ['title_ru', 'description_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky', 'description_ky'],
        }),
    )
    
admin.site.register(History, HistoryAdmin)

admin.site.register(Map)

class VacancyAdmin(TranslationAdmin):
    fieleds = [
        'title', 'description', 'description_detail'
    ]

admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(TypeInformation)

admin.site.register(Person)