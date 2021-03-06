# Generated by Django 3.0.9 on 2021-01-27 06:35

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=100, verbose_name='№ п/п')),
                ('code', models.CharField(max_length=300, verbose_name='Код услуги')),
                ('name', models.CharField(max_length=500, verbose_name='Наименование услуги')),
                ('price', models.CharField(max_length=100, verbose_name='Цена')),
                ('category', mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.PROTECT, to='services.Category', verbose_name='Подкатегория')),
            ],
        ),
    ]
