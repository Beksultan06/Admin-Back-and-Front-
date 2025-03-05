from modeltranslation.translator import register, TranslationOptions
from app.news.models import News, Media, NewsNok, TourismNok, AboutNok, Project

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description','first_paragraph','second_paragraph','general_paragraph')

@register(Media)
class MediaTranslationOptions(TranslationOptions):
    fields = ('title_media', 'description_media',)


@register(NewsNok)
class NewsNokTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'date')


@register(TourismNok)
class TourismNokTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(AboutNok)
class AboutNokTranslationOptions(TranslationOptions):
    fields = ('description',)

@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'description_detail')