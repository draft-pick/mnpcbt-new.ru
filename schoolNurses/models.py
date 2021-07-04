from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="Наименование категории")
    slug = models.SlugField(max_length=255, verbose_name="Url", unique=True)
    anons = RichTextUploadingField(blank=True, verbose_name='Анонс')
    content = RichTextUploadingField(blank=True, verbose_name='Контент')
    url = models.CharField(blank=True, max_length=300, verbose_name="Ссылка на документ")
    icon = models.CharField(blank=True, max_length=255, verbose_name="Иконка")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category_school_nurses', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class periods(models.Model):
    title = models.CharField(max_length=255, verbose_name="Наименование периода")
    start_date = models.DateField(auto_now=False, verbose_name="Дата начала обучения")
    end_date = models.DateField(auto_now=False, verbose_name="Дата окончания обучения")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('period_app_detail', kwargs={"period_app_id": self.pk})

    class Meta:
        verbose_name = 'Добавить период'
        verbose_name_plural = 'Добавление периода'


class contracts(models.Model):
    key_periods = models.ForeignKey(periods, on_delete=models.CASCADE, related_name='period_fk', verbose_name='Период')
    title = models.CharField(max_length=255, verbose_name="Номер контракта")
    contract_date = models.DateField(auto_now=False, verbose_name="Дата контракта")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Контракт'
        verbose_name_plural = 'Добавление контракта'


class management(models.Model):
    title = models.CharField(max_length=255, verbose_name="Учреждение|Рук-ль группы")
    man_key_periods = models.ForeignKey(periods, on_delete=models.CASCADE, related_name='man_period_fk',
                                        verbose_name='Период')
    man_key_contracts = models.ForeignKey(contracts, on_delete=models.CASCADE, related_name='man_contract_fk',
                                          verbose_name='Контракт')

    def __str__(self):
        return self.title


class form_registration(models.Model):
    reg_key_periods = models.ForeignKey(periods, on_delete=models.CASCADE, related_name='reg_period_fk',
                                        verbose_name='Период')
    reg_key_contract = models.ForeignKey(contracts, on_delete=models.CASCADE, related_name='reg_contract_fk',
                                         verbose_name='Контракт')
    reg_key_management = models.ForeignKey(management, on_delete=models.CASCADE, related_name='reg_management_fk',
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
