# Generated by Django 4.2.7 on 2025-02-17 13:51

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("managers", "0003_alter_schedule_options_catalog_description_detail_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="catalog",
            name="description_detail_ky",
            field=ckeditor.fields.RichTextField(
                null=True, verbose_name="Описание детально"
            ),
        ),
        migrations.AddField(
            model_name="catalog",
            name="description_detail_ru",
            field=ckeditor.fields.RichTextField(
                null=True, verbose_name="Описание детально"
            ),
        ),
    ]
