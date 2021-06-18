from django.db import models
from django.urls import reverse


class conference(models.Model):
    title = models.CharField(max_length=500, verbose_name='Наименование')

    def get_absolute_url(self):
        return reverse('view_conference', kwargs={"conference_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Добавить коференцию'
        verbose_name_plural = 'Добавить коференцию'


class schoolName(models.Model):
    title = models.CharField(max_length=500, verbose_name='Наименование')
    conference_key = models.ForeignKey(conference, on_delete=models.CASCADE, related_name='conference',
                                       verbose_name='Конференция')

    def get_absolute_url(self):
        return reverse('view_school', kwargs={"school_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Добавить школу'
        verbose_name_plural = 'Добавить школу'


class regSurname(models.Model):
    surname = models.CharField(max_length=500, verbose_name='Фамилия')
    school_key = models.ForeignKey(schoolName, on_delete=models.CASCADE, related_name='school',
                                   verbose_name='Школа')

    def get_absolute_url(self):
        return reverse('view_regConf', kwargs={"regconf_id": self.pk})

    def __str__(self):
        return self.surname

    class Meta:
        verbose_name = 'Добавить участника'
        verbose_name_plural = 'Добавить участника'


class regName(models.Model):
    name = models.CharField(max_length=500, verbose_name='Имя')
    surname_key = models.ForeignKey(regSurname, on_delete=models.CASCADE, related_name='name', verbose_name='Имя')


class regPatronymic(models.Model):
    patronymic = models.CharField(max_length=500, verbose_name='Отчество')
    name_key = models.ForeignKey(regName, on_delete=models.CASCADE, related_name='patronymic',
                                 verbose_name='Отчество')
