from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class Know(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    slug = models.SlugField(unique=True, verbose_name='URL')
    url = models.CharField(blank=True, max_length=500, verbose_name='Ссылка')
    sort = models.CharField(blank=True, max_length=10, verbose_name="Сортировка")
    anons = models.BooleanField(default=False, verbose_name="На главную")

    def get_absolute_url(self):
        return reverse('view_know', kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Это нужно знать'
        verbose_name_plural = 'Это нужно знать'
