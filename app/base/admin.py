from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import We_Invite_To_View, Gallery, Banner, LatestNews, Settings
from .translation import BannerTranslationOptions
# Register your models here.

class We_Invite_To_ViewAdmin(TranslationAdmin):
    fields = ('title', 'title_place', 'description_place', 'date_place', 
              'image_place'
    )
    
class GalleryAdmin(TranslationAdmin):
    fields = ('title_gallery', 'photo'
    )
    
admin.site.register(We_Invite_To_View)
admin.site.register(Gallery)

class BannerAdmin(TranslationAdmin):
    fieldsets = (
        ('Изображения', {
            'fields': ['image'],
        }),
        ('Русская версия', {
            'fields': ['title_ru', 'description_ru', 'full_name_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky', 'description_ky', 'full_name_ky'],
        }),
    )


class LatestNewsAdmin(TranslationAdmin):
    fieldsets = (
        ('Изображения', {
            'fields': ['image'],
        }),
        ('Русская версия', {
            'fields': ['title_ru', 'description_ru', ],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky', 'description_ky',],
        }),
        ('Дополнительно', {
            'fields': ['date'],  # Убедитесь, что поле date добавлено
        }),
    )


admin.site.register(Banner, BannerAdmin)
admin.site.register(LatestNews, LatestNewsAdmin)
admin.site.register(Settings)