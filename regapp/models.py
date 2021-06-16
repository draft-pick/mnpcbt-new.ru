from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class Registration(models.Model):
    surname = models.CharField(max_length=500, verbose_name='Фамилия')
    name = models.CharField(max_length=500, verbose_name='Имя')
    patronymic = models.CharField(max_length=500, verbose_name='Отчество')
    place_job = models.CharField(max_length=500, verbose_name='Место работы')
    position = models.CharField(max_length=500, verbose_name='Должность')
    degree = models.CharField(blank=True, max_length=500, verbose_name='Ученая степень|Научное звание')
    location = models.CharField(max_length=500, verbose_name='Регион')
    phone_job = models.CharField(max_length=500, verbose_name='Рабочий телефон')
    phone = models.CharField(blank=True, max_length=500, verbose_name='Телефон')
    email = models.CharField(max_length=500, verbose_name='E-mail')
    school_choice = (
        ('Без посещения школы', 'Без посещения школы'),
        ('Школа профессора Борисова: «Перспективы лечения больных туберкулезом в ближайшие десятилетия»',
         'Школа профессора Борисова: «Перспективы лечения больных туберкулезом в ближайшие десятилетия»'),
        ('Школа академика Литвинова «Современные методы этиологической диагностики микобактериальной инфекции»',
         'Школа академика Литвинова «Современные методы этиологической диагностики микобактериальной инфекции»'),
        ('«Особенности профилактики и лечения детского туберкулеза в мегаполисе»',
         '«Особенности профилактики и лечения детского туберкулеза в мегаполисе»'),
        ('«Организация работы среднего медицинского персонала в период пандемии»',
         '«Организация работы среднего медицинского персонала в период пандемии»'),
    )
    school = models.CharField(max_length=300, choices=school_choice, verbose_name='Школа')

    def get_absolute_url(self):
        return reverse('view_reg', kwargs={"reg_id": self.pk})

    def __str__(self):
        return self.surname

    class Meta:
        verbose_name = 'Регистрация на конференицию'
        verbose_name_plural = 'Регистрация на конференицию'
