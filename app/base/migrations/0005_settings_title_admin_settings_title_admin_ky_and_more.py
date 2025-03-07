# Generated by Django 4.2.7 on 2025-02-22 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_settings'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='title_admin',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Заголовка Авминитсратора'),
        ),
        migrations.AddField(
            model_name='settings',
            name='title_admin_ky',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Заголовка Авминитсратора'),
        ),
        migrations.AddField(
            model_name='settings',
            name='title_admin_ru',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Заголовка Авминитсратора'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='end_news',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Последний новости'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='end_news_ky',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Последний новости'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='end_news_ru',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Последний новости'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='gallery',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Галлерия'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='gallery_ky',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Галлерия'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='gallery_ru',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Галлерия'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='link_facebook',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылки на файсбук'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='link_insta',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылки на интсраграм'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='link_phone',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылки на номер телефона'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='link_telegram',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылки на телеграм'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='link_watapp',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылки на ватсап'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='link_youtube',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылки на ютуб'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='location',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Локация'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='location_ky',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Локация'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='location_ru',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Локация'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='settings', verbose_name='лого'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='news_nookat',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Носовти о Ноокат'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='news_nookat_ky',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Носовти о Ноокат'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='news_nookat_ru',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Носовти о Ноокат'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='номер телефона'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='preview',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Предосмотр'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='preview_ky',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Предосмотр'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='preview_ru',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Предосмотр'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='project_title',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Проекты'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='project_title_ky',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Проекты'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='project_title_ru',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Проекты'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='title_cmi',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='СМИ'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='title_cmi_ky',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='СМИ'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='title_cmi_ru',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='СМИ'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='title_logo',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Заголовка Логотипа'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='title_logo_ky',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Заголовка Логотипа'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='title_logo_ru',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Заголовка Логотипа'),
        ),
    ]
