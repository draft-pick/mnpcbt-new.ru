# Generated by Django 3.0.9 on 2021-05-17 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=500, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=500, verbose_name='Имя')),
                ('patronymic', models.CharField(max_length=500, verbose_name='Отчество')),
                ('post', models.CharField(max_length=500, verbose_name='Должность')),
                ('units', models.CharField(max_length=500, verbose_name='Подразделение')),
                ('branch', models.CharField(max_length=500, verbose_name='Филиал')),
                ('formation', models.CharField(max_length=500, verbose_name='Образование')),
                ('speciality', models.CharField(max_length=500, verbose_name='Специальность')),
                ('category', models.CharField(max_length=200, verbose_name='Категория')),
                ('degree', models.CharField(max_length=200, verbose_name='Ученая степень')),
                ('rank', models.CharField(max_length=200, verbose_name='Ученое звание')),
                ('mos_doc', models.CharField(max_length=200, verbose_name='Московский врач')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
                'ordering': ['surname'],
            },
        ),
    ]
