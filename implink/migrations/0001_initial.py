# Generated by Django 3.0.9 on 2020-11-24 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImpLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(blank=True, max_length=300, verbose_name='Контент')),
                ('image_title', models.ImageField(blank=True, upload_to='implink', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Важные ссылки',
                'verbose_name_plural': 'Важные ссылки',
            },
        ),
    ]
