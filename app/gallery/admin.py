from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from .translation import *
from .models import *

class GalleryNewShapesAdmin(TranslationAdmin):
    fieldsets = (
        ('Изображения', {
            'fields': ['image'],
        }),
    )
admin.site.register(GalleryNewShapes, GalleryNewShapesAdmin)

class GalleryOshTourAdmin(TranslationAdmin):
    fieldsets = (
        ('Изображения', {
            'fields': ['image', ],
        }),
        ('Ссылки', {
            'fields': ['link', ],
        }),
        ('Русская версия', {
            'fields': ['title_ru', ],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky', ],
        }),
    )

admin.site.register(GalleryOshTour, GalleryOshTourAdmin)

class GalleryArchivalPhotosAdmin(TranslationAdmin):
    fieldsets = (
        ('Изображения', {
            'fields': ['image'],
        }),
    )
admin.site.register(GalleryArchivalPhotos, GalleryArchivalPhotosAdmin)


class PhotoMiniAdmin(TranslationAdmin):
    fieldsets = (
        ('Изображения', {
            'fields': ['image', 'link'],
        }),
        ('Русская версия', {
            'fields': ['title_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky'],
        }),
    )

admin.site.register(PhotoMini, PhotoMiniAdmin)