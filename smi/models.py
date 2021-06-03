from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class smiArticles(models.Model):
    title = models.CharField(max_length=300, verbose_name='Наименование')
    url = models.CharField(max_length=500, verbose_name='Ссылка')
    created_at = models.DateTimeField(auto_now_add=False, verbose_name='Дата публикации')

    def get_absolute_url(self):
        return reverse('view_smi_article', kwargs={"smi_article_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class smiVideoclips(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    slug = models.SlugField(unique=True, verbose_name='URL')
    url = models.CharField(blank=True, max_length=500, verbose_name='Ссылка на внешний источник')
    sort = models.CharField(blank=True, max_length=10, verbose_name="Сортировка")
    content = RichTextUploadingField(blank=True, verbose_name='Контент')

    def get_absolute_url(self):
        return reverse('view_smi_videoclips', kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Видеоролик'
        verbose_name_plural = 'Видеоролики'
