from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class News(models.Model):
    title = models.TextField(verbose_name='Аталышы')
    image = models.ImageField(upload_to='news/')
    description = RichTextField(verbose_name='Сүрөттөлүшү')
    first_paragraph = RichTextField(verbose_name='Биринчи абзац')
    second_paragraph = RichTextField(verbose_name='Экинчи абзац')
    general_paragraph = RichTextField(verbose_name='Жалпы абзац')
    date = models.CharField(max_length=155, verbose_name='Дата')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Жаңылыктар'
        verbose_name_plural = 'Жаңылыктар'

class NewsObject(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name='Жаңылык')
    image = models.ImageField(upload_to='news/')

    def __str__(self):
        return str(self.news)

    class Meta:
        verbose_name = 'Сүрөттөр'
        verbose_name_plural = 'Сүрөттөр'

class Media(models.Model):
    title_media = models.CharField(max_length=100, verbose_name='ЖМК бетинин аталышы')
    description_media = RichTextField(verbose_name='ЖМК бетинин сүрөттөлүшү')
    date_media = models.CharField(max_length=155, verbose_name='ЖМК бетинин датасы')
    image_media = models.ImageField(upload_to='news/')
    link = models.URLField(verbose_name='Шилтеме')

    def __str__(self):
        return self.title_media

    class Meta:
        verbose_name = 'ЖМК'
        verbose_name_plural = 'ЖМК'

class NewsNok(models.Model):
    title = RichTextField(verbose_name='Аталышы')
    description = RichTextField(verbose_name='Сүрөттөлүшү')
    date = models.CharField(max_length=225, verbose_name='Дата')
    photo = models.ImageField(upload_to='news-nok/', verbose_name='Сүрөт')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Нок районунун жаңылыгы'
        verbose_name_plural = 'Нок районунун жаңылыктары'

class TourismNok(models.Model):
    title = RichTextField(verbose_name='Аталышы')
    description = RichTextField(verbose_name='Сүрөттөлүшү')
    image = models.ImageField(upload_to='tourism-nok/', verbose_name='Сүрөт')

class AboutNok(models.Model):
    description = RichTextField(verbose_name='Сүрөттөлүшү')
    image = models.ImageField(upload_to='about-nok/', verbose_name='Сүрөт')

    def __str__(self):
        return 'Нок району жөнүндө'

    class Meta:
        verbose_name = 'Нок району жөнүндө'
        verbose_name_plural = 'Нок району жөнүндө'

class Project(models.Model):
    title = models.CharField(max_length=255, verbose_name='Аталышы')
    image = models.ImageField(upload_to='project_images/', verbose_name='Сүрөт')
    date = models.CharField(max_length=100, verbose_name='Дата')
    description = RichTextField(verbose_name='Сүрөттөлүшү')
    description_detail = RichTextField(verbose_name='Толук сүрөттөлүшү')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Долбоор'
        verbose_name_plural = 'Долбоорлор'
