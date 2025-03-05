from django.contrib import admin
from .models import Managers
from .translation import *
from modeltranslation.admin import TranslationAdmin


# Register your models here.

class ManagersAdmin(TranslationAdmin):
    fieldsets = (
        ('Изображения', {
            'fields': ['image'],
        }),
        ('Русская версия', {
            'fields': ['full_name_ru', 'job_title_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['full_name_ky', 'job_title_ky'],
        }),
    )
admin.site.register(Managers, ManagersAdmin)

class Structure_adminsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Изображения', {
            'fields': ['image'],
        }),
        ('Русская версия', {
            'fields': ['title_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky'],
        }),
    )   
admin.site.register(Structure_admins, Structure_adminsAdmin)
class ScheduleAdmin(TranslationAdmin):
    fieldsets = (
        ('Общие данные', {  
            'fields': ['date'],  # Поле date теперь в отдельной секции
        }),
        ('Русская версия', {
            'fields': ['title_ru', 'description_ru', 'full_name_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky', 'description_ky', 'full_name_ky'],
        }),
    )
admin.site.register(Schedule, ScheduleAdmin)

class CatalogAdmin(TranslationAdmin):
    fieldsets = (
        ('Изображения', {
            'fields': ['image', 'date'],
        }),
        ('Русская версия', {
            'fields': ['title_ru', 'description_ru', 'description_detail_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky', 'description_ky', 'description_detail_ky'],
        }),
    )
admin.site.register(Catalog, CatalogAdmin)
