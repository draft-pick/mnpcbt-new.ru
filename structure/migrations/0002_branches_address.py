# Generated by Django 3.0.9 on 2020-12-25 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='branches',
            name='address',
            field=models.CharField(blank=True, max_length=500, verbose_name='Адрес'),
        ),
    ]