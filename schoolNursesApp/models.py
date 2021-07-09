from django.db import models
from django.urls import reverse


class periodsApp(models.Model):
    title = models.CharField(max_length=255, verbose_name="Наименование периода")
    start_date = models.DateField(auto_now=False, verbose_name="Дата начала обучения")
    end_date = models.DateField(auto_now=False, verbose_name="Дата окончания обучения")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('app_period_view', kwargs={"app_period_id": self.pk})

    class Meta:
        verbose_name = 'Период'
        verbose_name_plural = 'Период'


class contractsApp(models.Model):
    key_periods = models.ForeignKey(periodsApp, on_delete=models.CASCADE, related_name='periodApp_fk',
                                    verbose_name='Период')
    title = models.CharField(max_length=255, verbose_name="Номер контракта")
    contract_date = models.DateField(auto_now=False, verbose_name="Дата контракта")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Контракт'
        verbose_name_plural = 'Контракт'


class managementApp(models.Model):
    title = models.CharField(max_length=255, verbose_name="Учреждение|Рук-ль группы")
    man_key_periods = models.ForeignKey(periodsApp, on_delete=models.CASCADE, related_name='man_periodApp_fk',
                                        verbose_name='Период')
    man_key_contracts = models.ForeignKey(contractsApp, on_delete=models.CASCADE, related_name='man_contractApp_fk',
                                          verbose_name='Контракт')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('app_management_view', kwargs={"app_management_id": self.pk})


class otherApp(models.Model):
    reg_key_management = models.ForeignKey(managementApp, on_delete=models.CASCADE, related_name='reg_managementApp_fk',
                                           verbose_name='Учреждение|Рук-ль группы')
    surname = models.CharField(max_length=300, verbose_name='Фамилия')
    name = models.CharField(max_length=300, verbose_name='Имя')
    patronymic = models.CharField(max_length=300, verbose_name='Отчество')
    birthday = models.DateField(auto_now=False, verbose_name='Дата рождения')
    SEX = (
        ('Ж', 'Ж'),
        ('М', 'М'),
    )
    sex = models.CharField(max_length=1, choices=SEX, verbose_name='Пол')
    snils = models.CharField(max_length=100, verbose_name='СНИЛС')
