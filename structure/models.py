from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class Branches(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование')
    amb_help = RichTextUploadingField(blank=True, verbose_name="Амбулаторная помощь")
    stac_help = RichTextUploadingField(blank=True, verbose_name="Стационарная помощь")
    address = models.CharField(blank=True, max_length=500, verbose_name="Адрес")
    tel_cnt_br = models.CharField(blank=True, max_length=200, verbose_name="Телефоны контакта филиала")
    tel_hotline = models.CharField(blank=True, max_length=100, verbose_name="Горячая линия")
    secretary = models.CharField(blank=True, max_length=200, verbose_name="Секретарь тел./факс")
    tel_reg_ad = models.CharField(blank=True, max_length=100, verbose_name="Регистратура(взр-ое.отд.)")
    tel_reg_ch = models.CharField(blank=True, max_length=100, verbose_name="Регистратура(дет-ое.отд.)")
    email = models.CharField(blank=True, max_length=100, verbose_name="Электронная почта")
    opening_hour = RichTextUploadingField(blank=True, verbose_name="Режим работы")
    head = RichTextUploadingField(blank=True, verbose_name="Руководитель филилал")
    tel_head = models.CharField(blank=True, max_length=100, verbose_name="Телефоны контакта рукод-ва")
    reception = models.CharField(blank=True, max_length=100, verbose_name="Приемная")
    opening_hour_head = RichTextUploadingField(blank=True, verbose_name="Часы работы заведующего")
    substitute = RichTextUploadingField(blank=True, verbose_name="Заместитель/телефон/часы приема")
    substitute_info = RichTextUploadingField(blank=True, verbose_name="Информация о руководителях")
    history = RichTextUploadingField(blank=True, verbose_name="Краткая история")
    territory = RichTextUploadingField(blank=True, verbose_name="Территориальные районы")
    body_info = RichTextUploadingField(blank=True, verbose_name="Информация о корпусах")
    stac_info = RichTextUploadingField(blank=True, verbose_name="Информация о стационаре")
    doctors_info = RichTextUploadingField(blank=True, verbose_name="Количество врачей")
    otdel_info = RichTextUploadingField(blank=True, verbose_name="Информация по отделениям")
    separation_info = RichTextUploadingField(blank=True, verbose_name="Информация по кабинетам")
    type_help = RichTextUploadingField(blank=True, verbose_name="Виды помощи")
    equipping_info = RichTextUploadingField(blank=True, verbose_name="Оснащение филиала")
    medicines_info = RichTextUploadingField(blank=True, verbose_name="Информация о лекарствах")
    other_info = RichTextUploadingField(blank=True, verbose_name="Иная информация")
    anons_info = RichTextUploadingField(blank=True, verbose_name="Анонс")
    image_title = models.ImageField(upload_to='branches/', verbose_name='Фото заголовка', blank=True)
    image_head = models.ImageField(upload_to='branches/', verbose_name='Фото руководителя', blank=True)

    def get_absolute_url(self):
        return reverse('view_branch', kwargs={"branch_id": self.pk})

    def get_spec_url(self):
        return reverse('view_specialist', kwargs={"branch_id": self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Филиал'
        verbose_name_plural = 'Филиалы'


class GalleryBranches(models.Model):
    image = models.ImageField(upload_to='branches/', verbose_name='Фото/Схема проезда', blank=True)
    keyBranches = models.ForeignKey(Branches, on_delete=models.CASCADE, related_name='images')
    location_map = models.BooleanField(default=False, verbose_name='Схема проезда')


class Specialists(models.Model):
    keyBranches = models.ForeignKey(Branches, on_delete=models.CASCADE, related_name='specialist', verbose_name='Филиал')
    surname = models.CharField(max_length=100, verbose_name='Фамилия')
    name = models.CharField(max_length=100, verbose_name='Имя')
    patronymic = models.CharField(blank=True, max_length=100, verbose_name='Отчество')
    division = models.CharField(blank=True, max_length=300, verbose_name='Подразделение (Наименование)')
    job = models.CharField(blank=True, max_length=200, verbose_name='Штатная должность (Наименование)')
    vyz = models.CharField(blank=True, max_length=300, verbose_name='ВУЗ')
    date_vyz = models.CharField(blank=True, max_length=100, verbose_name='Дата окончания')
    profession = models.CharField(blank=True, max_length=200, verbose_name='Специальность')
    sertif = models.CharField(blank=True, max_length=100, verbose_name='Сертификат')
    date_sertif = models.CharField(blank=True, max_length=100, verbose_name='Дата выдачи')
    category = models.CharField(blank=True, max_length=100, verbose_name='Категория')
    degree = models.CharField(blank=True, max_length=100, verbose_name='Степень')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Специалист'
        verbose_name_plural = 'Специалисты'
