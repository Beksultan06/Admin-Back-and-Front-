# Generated by Django 4.2.7 on 2025-02-16 08:51

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=135, verbose_name='Заголовок')),
                ('title_ru', models.CharField(max_length=135, null=True, verbose_name='Заголовок')),
                ('title_ky', models.CharField(max_length=135, null=True, verbose_name='Заголовок')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Описание Общей Информации')),
                ('description_ru', ckeditor.fields.RichTextField(null=True, verbose_name='Описание Общей Информации')),
                ('description_ky', ckeditor.fields.RichTextField(null=True, verbose_name='Описание Общей Информации')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Общая Информация',
                'verbose_name_plural': 'Общая Информация',
            },
        ),
        migrations.CreateModel(
            name='HeadPersonality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_personality', models.CharField(max_length=100, verbose_name='Заголовок ВЛР ')),
                ('title_personality_ru', models.CharField(max_length=100, null=True, verbose_name='Заголовок ВЛР ')),
                ('title_personality_ky', models.CharField(max_length=100, null=True, verbose_name='Заголовок ВЛР ')),
                ('image_personality', models.ImageField(upload_to='personalities/', verbose_name='Изображение ВЛР')),
            ],
            options={
                'verbose_name': 'Выдвющиеся личности района',
                'verbose_name_plural': 'Выдвющиеся личности района',
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок для "История района"')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='Заголовок для "История района"')),
                ('title_ky', models.CharField(max_length=255, null=True, verbose_name='Заголовок для "История района"')),
                ('image', models.ImageField(upload_to='history_images/', verbose_name='Фото для "История айона"')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Описание для "История района"')),
                ('description_ru', ckeditor.fields.RichTextField(null=True, verbose_name='Описание для "История района"')),
                ('description_ky', ckeditor.fields.RichTextField(null=True, verbose_name='Описание для "История района"')),
            ],
            options={
                'verbose_name': 'История района',
                'verbose_name_plural': 'История районов',
            },
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Заголовок')),
                ('title_ru', models.TextField(null=True, verbose_name='Заголовок')),
                ('title_ky', models.TextField(null=True, verbose_name='Заголовок')),
                ('image', models.ImageField(upload_to='op/')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Описание')),
                ('description_ru', ckeditor.fields.RichTextField(null=True, verbose_name='Описание')),
                ('description_ky', ckeditor.fields.RichTextField(null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Айылных маймаков',
                'verbose_name_plural': 'Айылных маймаков',
            },
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Заголовок')),
                ('title_ru', models.TextField(null=True, verbose_name='Заголовок')),
                ('title_ky', models.TextField(null=True, verbose_name='Заголовок')),
                ('image', models.ImageField(upload_to='locations/')),
                ('link', models.URLField(verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Карта района',
            },
        ),
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок для "Паспорт района"')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='Заголовок для "Паспорт района"')),
                ('title_ky', models.CharField(max_length=255, null=True, verbose_name='Заголовок для "Паспорт района"')),
                ('image', models.ImageField(upload_to='passport_images/', verbose_name='Фото для "Паспорт района"')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Описание для "Паспорт района"')),
                ('description_ru', ckeditor.fields.RichTextField(null=True, verbose_name='Описание для "Паспорт района"')),
                ('description_ky', ckeditor.fields.RichTextField(null=True, verbose_name='Описание для "Паспорт района"')),
            ],
            options={
                'verbose_name': 'Паспорт района',
                'verbose_name_plural': 'Паспорта районов',
            },
        ),
        migrations.CreateModel(
            name='Personality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_person', models.CharField(max_length=100, verbose_name='Имя личности')),
                ('name_person_ru', models.CharField(max_length=100, null=True, verbose_name='Имя личности')),
                ('name_person_ky', models.CharField(max_length=100, null=True, verbose_name='Имя личности')),
                ('description_person', models.TextField(verbose_name='Описание личности')),
                ('description_person_ru', models.TextField(null=True, verbose_name='Описание личности')),
                ('description_person_ky', models.TextField(null=True, verbose_name='Описание личности')),
                ('image_person', models.ImageField(upload_to='personalities/', verbose_name='Изображение личности')),
                ('all_description_person', ckeditor.fields.RichTextField(verbose_name='Полное описание личности')),
                ('all_description_person_ru', ckeditor.fields.RichTextField(null=True, verbose_name='Полное описание личности')),
                ('all_description_person_ky', ckeditor.fields.RichTextField(null=True, verbose_name='Полное описание личности')),
            ],
            options={
                'verbose_name': 'Личность',
                'verbose_name_plural': 'Личности',
            },
        ),
        migrations.CreateModel(
            name='TypeInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='Тип Информаций')),
                ('title_ru', models.CharField(max_length=155, null=True, verbose_name='Тип Информаций')),
                ('title_ky', models.CharField(max_length=155, null=True, verbose_name='Тип Информаций')),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Заголовок вакансии')),
                ('title_ru', models.TextField(null=True, verbose_name='Заголовок вакансии')),
                ('title_ky', models.TextField(null=True, verbose_name='Заголовок вакансии')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Описание вакансий')),
                ('description_ru', ckeditor.fields.RichTextField(null=True, verbose_name='Описание вакансий')),
                ('description_ky', ckeditor.fields.RichTextField(null=True, verbose_name='Описание вакансий')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Вакансия',
            },
        ),
    ]
