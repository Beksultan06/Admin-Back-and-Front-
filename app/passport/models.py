from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Passport(models.Model):
    title = models.CharField(max_length=255, verbose_name='Паспорт району аталышы')
    image = models.ImageField(upload_to='passport_images/', verbose_name='Паспорт району сүрөтү')
    description = RichTextField(verbose_name='Паспорт району сүрөттөлүшү')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Паспорт району'
        verbose_name_plural = 'Паспорттор райондор'

class GeneralInformation(models.Model):
    title = models.CharField(max_length=135, verbose_name='Жалпы маалымат аталышы')
    description = RichTextField(verbose_name='Жалпы маалымат сүрөттөлүшү')
    image = models.ImageField(upload_to='images/', verbose_name='Сүрөт')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Жалпы маалымат'
        verbose_name_plural = 'Жалпы маалымат'

class GeneralInformationImage(models.Model):
    general_information = models.ForeignKey(GeneralInformation, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/', verbose_name='Сүрөт')

    class Meta:
        verbose_name = 'Сүрөт'
        verbose_name_plural = 'Сүрөттөр'

class Info(models.Model):
    title = models.TextField(verbose_name='Аталышы')
    image = models.ImageField(upload_to='image/')
    description = RichTextField(verbose_name='Сүрөттөлүшү')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Айылдык аймактар'
        verbose_name_plural = 'Айылдык аймактар'

class InfoObject(models.Model):
    info = models.ForeignKey(Info, on_delete=models.CASCADE, verbose_name='Маалымат')
    image = models.ImageField(upload_to='image/')

    class Meta:
        verbose_name = 'Сүрөт'
        verbose_name_plural = 'Маалымат сүрөттөрү'

class HeadPersonality(models.Model):
    title_personality = models.CharField(max_length=100, verbose_name='Атактуулар аталышы')
    image_personality = models.ImageField(upload_to='personalities/', verbose_name='Атактуулар сүрөтү')

    def __str__(self):
        return self.title_personality

    class Meta:
        verbose_name = 'Атактуу адамдар'
        verbose_name_plural = 'Атактуу адамдар'

class Personality(models.Model):
    name_person = models.CharField(max_length=100, verbose_name='Адамдын аты')
    description_person = models.TextField(verbose_name='Адамдын сүрөттөлүшү')
    image_person = models.ImageField(upload_to='personalities/', verbose_name='Адамдын сүрөтү')
    all_description_person = RichTextField(verbose_name='Адамдын толук сүрөттөлүшү')

    def __str__(self):
        return 'Атактуу адам: ' + self.name_person

    class Meta:
        verbose_name = 'Атактуу адам'
        verbose_name_plural = 'Атактуу адамдар'

class History(models.Model):
    title = models.CharField(max_length=255, verbose_name='Тарых аталышы')
    image = models.ImageField(upload_to='history_images/', verbose_name='Тарых сүрөтү')
    description = RichTextField(verbose_name='Тарых сүрөттөлүшү')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тарых'
        verbose_name_plural = 'Тарыхтар'

class Map(models.Model):
    title = models.TextField(verbose_name='Карта аталышы')
    image = models.ImageField(upload_to='locations/')
    link = models.URLField(verbose_name='Шилтеме')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Карта'
        verbose_name_plural = 'Карталар'

class Vacancy(models.Model):
    title = models.TextField(verbose_name='Вакансия аталышы')
    description = RichTextField(verbose_name='Вакансия сүрөттөлүшү')
    description_detail = RichTextField(verbose_name='Вакансия сүрөттөлүшү толук маалымат')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансиялар'

class Person(models.Model):
    title = models.CharField(max_length=155, verbose_name='Маалымат түрү')
    img = models.ImageField(upload_to='type', verbose_name='Сүрөт')
    description = RichTextField(verbose_name='Сүрөттөлүшү')
    description_detail = RichTextField(verbose_name='Толук сүрөттөлүшү')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Атактуу адамдар'
        verbose_name_plural = 'Атактуу адамдар'

class TypeInformation(models.Model):
    title = models.CharField(max_length=155, verbose_name='Маалымат түрү')
    img = models.ImageField(upload_to='type', verbose_name='Сүрөт', blank=True, null=True)
    description = RichTextField(verbose_name='Сүрөттөлүшү', blank=True, null=True)
    person = models.ManyToManyField(Person, related_name='districts', verbose_name='Атактуу адамдар', blank=True, null=True)
    link = models.URLField(verbose_name='Шилтеме', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Маалымат түрү'
        verbose_name_plural = 'Маалымат түрлөрү'
