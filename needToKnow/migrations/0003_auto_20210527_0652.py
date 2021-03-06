# Generated by Django 3.0.9 on 2021-05-27 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('needToKnow', '0002_auto_20210527_0633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='know',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='know',
            name='title',
            field=models.CharField(max_length=250, verbose_name='Заголовок'),
        ),
    ]
