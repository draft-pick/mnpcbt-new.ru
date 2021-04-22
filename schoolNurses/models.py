from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="Наименование категории")
    slug = models.SlugField(max_length=255, verbose_name="Url", unique=True)
    anons = RichTextUploadingField(blank=True, verbose_name='Анонс')
    content = RichTextUploadingField(blank=True, verbose_name='Контент')
    url = models.CharField(blank=True, max_length=300, verbose_name="Ссылка на документ")
    icon = models.CharField(blank=True, max_length=255, verbose_name="Иконка")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category_school_nurses', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


