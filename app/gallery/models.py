from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class GalleryNewShapes(models.Model):
    image = models.ImageField(
        upload_to='gallery_photos/',
        verbose_name='Жаңы фигуралардын сүрөтү'
    )

    def __str__(self):
        return f"Сүрөт {self.id}"

    class Meta:
        verbose_name = 'Жаңы сүрөттөр'
        verbose_name_plural = 'Жаңы сүрөттөр'

class GalleryOshTour(models.Model):
    title = models.CharField(
        max_length=135,
        verbose_name='Ош Турдун аталышы'
    )
    image = models.ImageField(
        upload_to='gallery_images/',
        verbose_name='Ош Турдун сүрөтү'
    )
    link = models.URLField(
        verbose_name='Шилтеме'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '3D Тур'
        verbose_name_plural = '3D Тур'

class GalleryArchivalPhotos(models.Model):
    image = models.ImageField(
        upload_to='gallery_photos/',
        verbose_name='Архивдик сүрөт'
    )

    def __str__(self):
        return f"Сүрөт {self.id}"

    class Meta:
        verbose_name = 'Тарыхый сүрөттөр'
        verbose_name_plural = 'Тарыхый сүрөттөр'

class PhotoMini(models.Model):
    title = RichTextField(  
        verbose_name='Аталышы'
    )
    image = models.ImageField(
        upload_to='photo_kg/',
        verbose_name='Сүрөт'
    )
    link = models.URLField(
        verbose_name='шилтеме'
    )
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural='Өнөктөштөр'
