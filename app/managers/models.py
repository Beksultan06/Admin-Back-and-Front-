from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Managers(models.Model):
    full_name = models.CharField(verbose_name='Толук аты-жөнү', max_length=255)
    job_title = models.CharField(verbose_name='Кызматы', max_length=255)
    image = models.ImageField(verbose_name='Сүрөт', upload_to='managers_img/')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Жетекчи'
        verbose_name_plural = 'Жетекчилер'

class Structure_admins(models.Model):
    title = models.CharField(
        max_length=255, 
        verbose_name='Администрациянын түзүмү'
    )
    image = models.ImageField(
        verbose_name='Сүрөт', 
        upload_to='managers_img/'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Администрациянын түзүмү'
        verbose_name_plural = 'Администрациянын түзүмдөрү'

class Schedule(models.Model):
    title = models.CharField(max_length=100, verbose_name='Темасы')
    description = models.TextField(verbose_name='Сүрөттөлүшү')
    date = models.CharField(max_length=155, verbose_name='Убактысы')
    full_name = models.CharField(max_length=100, verbose_name='Толук аты-жөнү')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Жарандарды кабыл алуу графиги'
        verbose_name_plural = 'Жарандарды кабыл алуу графиги'

class Catalog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Аталышы')
    description = RichTextField(verbose_name='Сүрөттөлүшү')
    date = models.CharField(max_length=155, verbose_name='Убактысы')
    image = models.ImageField(verbose_name='Сүрөт', upload_to='managers_img/')
    description_detail = RichTextField(verbose_name='Толук сүрөттөлүшү')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталогдор'