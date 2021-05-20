from django.db import models
from django.urls import reverse


class Employees(models.Model):
    surname = models.CharField(max_length=500, verbose_name='Фамилия')
    name = models.CharField(max_length=500, verbose_name='Имя')
    patronymic = models.CharField(max_length=500, verbose_name='Отчество')
    post = models.CharField(max_length=500, verbose_name='Должность')
    units = models.CharField(max_length=500, verbose_name='Подразделение')
    branch = models.CharField(max_length=500, verbose_name='Филиал')
    formation = models.CharField(max_length=500, verbose_name='Образование')
    speciality = models.CharField(max_length=500, verbose_name='Специальность')
    category = models.CharField(max_length=200, blank=True, verbose_name='Категория')
    degree = models.CharField(max_length=200, blank=True, verbose_name='Ученая степень')
    rank = models.CharField(max_length=200, blank=True, verbose_name='Ученое звание')
    mos_doc = models.CharField(max_length=200, blank=True, verbose_name='Московский врач')
    mos_doc_url = models.CharField(max_length=500, blank=True, verbose_name="Ссылка на московского врача")

    def get_absolute_url(self):
        return reverse('view_employee', kwargs={"employee_id": self.pk})

    def __str__(self):
        return self.surname

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ['surname']


