from django.db import models
from  django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=255, verbose_name='Название категории')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})

    class MPTTMeta:
        order_insertion_by = ['name']


class Services(models.Model):
    number = models.CharField(max_length=100, verbose_name='№ п/п')
    code = models.CharField(max_length=300, verbose_name='Код услуги')
    name = models.CharField(max_length=500, verbose_name='Наименование услуги')
    price = models.CharField(max_length=100, verbose_name='Цена')
    category = TreeForeignKey(Category, on_delete=models.PROTECT, verbose_name='Подкатегория')

    def __str__(self):
        return self.name

