from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class We_Invite_To_View(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Биз көрүүгө сунуштайбыз"
    )
    title_place = models.CharField(
        max_length=255,
        verbose_name="Көрүү жайынын аталышы"
    )
    description_place = models.CharField(
        max_length=255,
        verbose_name="Көрүү жайынын сүрөттөлүшү"
    )
    date_place = models.CharField(
        max_length=155,
        verbose_name="Көрүү жайынын датасы"
    )
    image_place = models.ImageField(
        upload_to='base/',
        verbose_name="Көрүү жайынын сүрөтү"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Биз көрүүгө сунуштайбыз"
        verbose_name_plural = "Биз көрүүгө сунуштайбыз"

class Gallery(models.Model):
    title_gallery = models.CharField(   
        max_length=255,
        verbose_name="Галереянын аталышы"
    )
    photo = models.ImageField(
        upload_to='base/',
        verbose_name="Сүрөт"
    )
    def __str__(self):
        return self.title_gallery

    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галерея"

class Banner(models.Model):
    title = models.CharField(max_length=200, verbose_name='Баннердин аталышы')
    image = models.ImageField(upload_to='banner_images/', verbose_name='Баннердин сүрөтү')
    full_name = models.CharField(max_length=200, verbose_name='Толук аты-жөнү')
    description = RichTextField(verbose_name='Сүрөттөлүшү')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннер'

class LatestNews(models.Model):
    title = models.CharField(max_length=200, verbose_name='Жаңылыктын аталышы')
    image = models.ImageField(upload_to='latest_news_images/', verbose_name='Жаңылыктын сүрөтү')
    description = RichTextField(verbose_name='Сүрөттөлүшү')
    date = models.CharField(max_length=100,verbose_name='Дата')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Акыркы жаңылыктар'
        verbose_name_plural = 'Акыркы жаңылыктар'


class Settings(models.Model):
    logo = models.ImageField(upload_to='settings', verbose_name='лого', blank=True, null=True)
    title_logo = models.CharField(max_length=155,verbose_name='Заголовка Логотипа', blank=True, null=True)
    location = models.CharField(max_length=155,verbose_name='Локация', blank=True, null=True)
    phone = models.CharField(max_length=20, verbose_name='номер телефона', blank=True, null=True)
    link_phone  = models.URLField(verbose_name='Ссылки на номер телефона', blank=True, null=True)
    link_insta = models.URLField(verbose_name='Ссылки на интсраграм', blank=True, null=True)
    link_telegram = models.URLField(verbose_name='Ссылки на телеграм', blank=True, null=True)
    link_watapp = models.URLField(verbose_name='Ссылки на ватсап', blank=True, null=True)
    link_youtube = models.URLField(verbose_name='Ссылки на ютуб', blank=True, null=True)
    link_facebook = models.URLField(verbose_name='Ссылки на файсбук', blank=True, null=True)
    end_news = models.CharField(max_length=255,verbose_name='Последний новости', blank=True, null=True)
    preview = models.CharField(max_length=255,verbose_name='Предосмотр', blank=True, null=True)
    gallery = models.CharField(max_length=255,verbose_name='Галлерия', blank=True, null=True)
    news_nookat = models.CharField(max_length=255,verbose_name='Носовти о Ноокат', blank=True, null=True)
    title_cmi = models.CharField(max_length=255,verbose_name='СМИ', blank=True, null=True)
    project_title = models.CharField(max_length=255,verbose_name='Проекты', blank=True, null=True)
    title_admin = models.CharField(max_length=255,verbose_name='Заголовка Авминитсратора', blank=True, null=True)
    location_name = models.CharField(max_length=255, verbose_name='Заголовка Локация', blank=True, null=True)
    anti_corup = models.CharField(max_length=255,verbose_name='Антикорупций', blank=True, null=True)

    def __str__(self):
        return self.end_news

    class Meta:
        verbose_name_plural='Главная настройка'