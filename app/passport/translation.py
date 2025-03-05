from modeltranslation.translator import register, TranslationOptions
from .models import *
from modeltranslation.translator import register, TranslationOptions
from app.passport.models import *


@register(Passport)
class PassportTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'description',
    )

@register(GeneralInformation)
class GeneralInformationTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'description',
    )

@register(Info)
class InfoTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'description',
    )



@register(HeadPersonality)
class HeadPersonalityTranslationOptions(TranslationOptions):
    fields = (
        'title_personality',
    )


@register(Personality)
class PersonalityTranslationOptions(TranslationOptions):
    fields = (
        'name_person',
        'description_person',
        'all_description_person',
    )

@register(History)
class HistoryTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'description',
    )

@register(Map)
class Map(TranslationOptions):
    fields = (
        'title',
    )

@register(Vacancy)
class VacancyTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'description',
        'description_detail',
    )

@register(TypeInformation)
class TypeInformationTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'description',
    )

@register(Person)
class PersonTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'description',
        'description_detail',
    )
