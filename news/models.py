from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models import Q


class NewsManager(models.Manager):
    use_for_related_fields = True

    def search(self, query=None):
        qs = self.get_queryset()
        if query:
            or_lookup = (Q(title__icontains=query))
            qs = qs.filter(or_lookup)
        return qs


class News(models.Model):
    title = models.CharField(max_length=250, verbose_name='Наименование')
    slug = models.SlugField(unique=False, verbose_name='URL')
    anons = models.TextField(blank=True, verbose_name='Анонс')
    content = RichTextUploadingField(blank=True, verbose_name='Контент')
    created_at = models.DateField(auto_now_add=False, verbose_name='Дата публикации')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовать')
    image_title = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    tag = models.CharField(max_length=300, default=True, verbose_name='Опубликовать')
    objects = NewsManager()

    def get_absolute_url(self):
        return reverse('view_news', kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class GalleryNews(models.Model):
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    product = models.ForeignKey(News, on_delete=models.CASCADE, related_name='images')
