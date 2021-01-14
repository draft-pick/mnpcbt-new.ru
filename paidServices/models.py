from django.db import models
from django.urls import reverse


class PSCategory(models.Model):
    nameC = models.CharField(max_length=300, verbose_name='Наименование категории')

    def get_absolute_url(self):
        return reverse('view_psupcat', kwargs={"pscategory_id": self.pk})

    def __str__(self):
        return self.nameC

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class PSunderCategory(models.Model):
    nameUC = models.CharField(max_length=500, verbose_name='Наименование подкатегории')
    keyNameC = models.ForeignKey(PSCategory, on_delete=models.CASCADE, related_name='psundercategory',
                                 verbose_name='Подкатегория')

    def get_absolute_url(self):
        return reverse('view_psupcat', kwargs={"pscategory_id": self.pk})

    def get_service_url(self):
        return reverse('view_service', kwargs={"service_id": self.pk})

    def __str__(self):
        return self.nameUC

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class PSlist(models.Model):
    number = models.CharField(max_length=100, verbose_name='№ п/п')
    code = models.CharField(max_length=300, verbose_name='Код услуги')
    name = models.CharField(max_length=500, verbose_name='Наименование услуги')
    price = models.CharField(max_length=100, verbose_name='Цена')
    keyNameCU = models.ForeignKey(PSunderCategory, on_delete=models.CASCADE, related_name='psservice',
                                 verbose_name='Подкатегория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Наименование услуги'
        verbose_name_plural = 'Наименование услуги'
