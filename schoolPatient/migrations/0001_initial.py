# Generated by Django 3.0.9 on 2021-04-12 09:12

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sanatoriums',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Наименование')),
                ('address', models.CharField(max_length=250, verbose_name='Адрес')),
                ('site', models.CharField(max_length=250, verbose_name='Сайт')),
                ('type', models.CharField(max_length=250, verbose_name='Тип климатического курорта')),
                ('numbers', models.CharField(max_length=250, verbose_name='Номерной фонд')),
                ('typesTreatment', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Виды лечения')),
                ('indications', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Показания')),
                ('image_title', models.ImageField(blank=True, upload_to='photos/sanatoriums/', verbose_name='Фото')),
                ('image_diagram', models.ImageField(blank=True, upload_to='photos/sanatoriums/', verbose_name='Схема')),
            ],
            options={
                'verbose_name': 'Санаторий',
                'verbose_name_plural': 'Санатории',
            },
        ),
    ]
