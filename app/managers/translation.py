from modeltranslation.translator import register, TranslationOptions
from .models import Managers, Structure_admins, Schedule, Catalog

@register(Managers)
class ManagersTranslationOptions(TranslationOptions):
    fields = ('full_name', 'job_title',)
    
@register(Structure_admins)
class Structure_adminsTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(Schedule)
class ScheduleTranslationOptions(TranslationOptions):
    fields = ('title','full_name','description')


@register(Catalog)
class CatalogTranslationOptions(TranslationOptions):
    fields = ('title','description', 'description_detail')