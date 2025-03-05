from django.contrib import admin
from app.news.models import News, Media, NewsNok, TourismNok, AboutNok, Project, NewsObject
from modeltranslation.admin import TranslationAdmin
from django.forms import ModelForm, BaseInlineFormSet
# Register your models here.

class NewsAdminForm(ModelForm):
    class Meta:
        model = News
        fields = '__all__'

class NewsObjectInlineFormSet(BaseInlineFormSet):
    def add_fields(self, form, index):
        super().add_fields(form, index)
        if index is not None and index > 0:
            form.fields['image'].widget = admin.widgets.AdminFileWidget(attrs={'style': 'display:none;'})
            form.fields['image'].required = False

class NewsObjectInline(admin.TabularInline):
    model = NewsObject
    formset = NewsObjectInlineFormSet
    extra = 1

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if qs.exists():
            first_object = qs.first()
            return qs.exclude(id=first_object.id)
        return qs

    def get_fieldsets(self, request, obj=None):
        return (
            ('Изображение', {
                'fields': ('image',),
            }),
        )

class NewsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Кыргызкая версия', {
            'fields': ('title_ky', 'description_ky', 'date', 'first_paragraph_ky', 'second_paragraph_ky', 'general_paragraph_ky', 'image'),
        }),
        ('Русская версия', {
            'fields': ('title_ru', 'description_ru', 'first_paragraph_ru', 'second_paragraph_ru', 'general_paragraph_ru'),
        }),
    )
    inlines = [NewsObjectInline]

admin.site.register(News, NewsAdmin)

class MediaAdmin(TranslationAdmin):
    fields = ['title_media','description_media', 'date_media','image_media', 'link']

admin.site.register(Media)

class NewsNokAdmin(TranslationAdmin):
    fields = ['title', 'description', 'date', 'photo']

admin.site.register(NewsNok)

class TourismNokAdmin(TranslationAdmin):
    fields = ['title', 'description', 'image']

admin.site.register(TourismNok)

class AboutNokAdmin(TranslationAdmin): 
    fields = ['description', 'image']

admin.site.register(AboutNok)

class ProjectAdmin(TranslationAdmin):
    fields = ['title', 'description', 'date', 'image', 'description_detail']
    
admin.site.register(Project)