# Generated by Django 3.0.9 on 2021-07-07 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trainingNurses', '0003_personnurses_per_key_contract'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personnurses',
            name='per_key_management',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='per_managementNurses_fk', to='trainingNurses.managementNurses', verbose_name='Учреждение|Рук-ль группы'),
        ),
    ]
