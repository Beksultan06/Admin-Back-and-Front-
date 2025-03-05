from modeltranslation.translator import register, TranslationOptions
from .models import GalleryNewShapes, GalleryOshTour, GalleryArchivalPhotos, PhotoMini

@register(GalleryNewShapes)
class GalleryNewShapesTranslationOptions(TranslationOptions):
    fields = ('image',)  

@register(GalleryOshTour)
class GalleryOshTourTranslationOptions(TranslationOptions):
    fields = ('title', 'image', 'link',)

@register(GalleryArchivalPhotos)
class GalleryArchivalPhotosTranslationOptions(TranslationOptions):
    fields = ('image',)

@register(PhotoMini)
class PhotoTranslationOptions(TranslationOptions):
    fields = ('title',)
