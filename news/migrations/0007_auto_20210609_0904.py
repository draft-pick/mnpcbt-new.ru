# Generated by Django 3.0.9 on 2021-06-09 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_news_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='created_at',
            field=models.DateTimeField(verbose_name='Дата публикации'),
        ),
    ]