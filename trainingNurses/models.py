from django.db import models
from django.urls import reverse


class periodsNurses(models.Model):
    title = models.CharField(max_length=255, verbose_name="Наименование периода")
    start_date = models.DateField(auto_now=False, verbose_name="Дата начала обучения")
    end_date = models.DateField(auto_now=False, verbose_name="Дата окончания обучения")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('period_nurses_view', kwargs={"period_nurses_id": self.pk})

    class Meta:
        verbose_name = 'Период'
        verbose_name_plural = 'Период'


class contractsNurses(models.Model):
    title = models.CharField(max_length=255, verbose_name="Номер контракта")
    contract_date = models.DateField(auto_now=False, verbose_name="Дата контракта")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('contract_nurses_view', kwargs={"contract_nurses_id": self.pk})

    class Meta:
        verbose_name = 'Контракт'
        verbose_name_plural = 'Контракт'


class managementNurses(models.Model):
    title = models.CharField(max_length=255, verbose_name="Учреждение | Организатор группы")
    man_key_periods = models.ForeignKey(periodsNurses, on_delete=models.CASCADE, related_name='man_periodNurses_fk',
                                        verbose_name='Период')
    man_key_contracts = models.ForeignKey(contractsNurses, on_delete=models.CASCADE,
                                          related_name='man_contractNurses_fk', verbose_name='Контракт')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('management_nurses_view', kwargs={"management_nurses_id": self.pk})


class personNurses(models.Model):
    per_key_period = models.ForeignKey(periodsNurses, on_delete=models.CASCADE, related_name='per_periodNurses_fk',
                                       verbose_name='Период обучения')
    per_key_contract = models.ForeignKey(contractsNurses, on_delete=models.CASCADE, related_name='per_contactNurses_fk',
                                         verbose_name='Контракт')
    per_key_management = models.ForeignKey(managementNurses, on_delete=models.CASCADE,
                                           related_name='per_managementNurses_fk',
                                           verbose_name='Учреждение|Рук-ль группы',
                                           null=True,
                                           blank=True,)
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

    def get_absolute_url(self):
        return reverse('person_view', kwargs={"person_id": self.pk})
