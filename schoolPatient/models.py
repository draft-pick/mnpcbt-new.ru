from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class Sanatoriums(models.Model):
    title = models.CharField(max_length=250, verbose_name='Наименование')
    address = models.CharField(max_length=250, verbose_name='Адрес')
    site = models.CharField(max_length=250, verbose_name='Сайт')
    type = models.CharField(max_length=250, verbose_name='Тип климатического курорта')
    numbers = models.CharField(max_length=250, verbose_name='Номерной фонд')
    typesTreatment = RichTextUploadingField(blank=True, verbose_name='Виды лечения')
    indications = RichTextUploadingField(blank=True, verbose_name='Показания')
    image_title = models.ImageField(upload_to='photos/sanatoriums/', verbose_name='Фото', blank=True)
    image_diagram = models.ImageField(upload_to='photos/sanatoriums/', verbose_name='Схема', blank=True)

    def get_absolute_url(self):
        return reverse('view_sanatorium', kwargs={"sanatorium_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Санаторий'
        verbose_name_plural = 'Санатории'
