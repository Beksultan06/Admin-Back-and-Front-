from modeltranslation.translator import TranslationOptions, register
from app.base.models import We_Invite_To_View, Gallery, Banner, LatestNews, Settings

@register(We_Invite_To_View)
class We_Invite_To_ViewTranslationOptions(TranslationOptions):
    fields = (
        'title', 
        'title_place', 
        'description_place', 
        )

@register(Gallery)
class GalleryTranslationOptions(TranslationOptions):
    fields = (
        'title_gallery',
        )

@register(Banner)
class BannerTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'full_name',)

@register(LatestNews)
class LatestNewsTranslationOptions(TranslationOptions):
    fields = ('title', 
                'description',)

@register(Settings)
class SettingsTranslationOptions(TranslationOptions):
    fields = (
        'title_logo', 'location', 'end_news', 'preview', 'gallery', 'news_nookat', 'title_cmi', 'project_title', "title_admin", 'location_name', 'anti_corup'
    )