# Generated by Django 4.0.4 on 2022-05-30 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImportPlantsToggle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_import', models.BooleanField(default=True, verbose_name='Для запуска импорта просто сохраните объект')),
            ],
            options={
                'verbose_name': 'Запуск импорта',
                'verbose_name_plural': 'Запуск импорта',
            },
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата погрузки')),
                ('weight', models.FloatField(verbose_name='Вес (тн)')),
                ('status', models.CharField(blank=True, choices=[('U', 'Выгрузился'), ('R', 'Возврат')], max_length=15, verbose_name='Статус')),
                ('upd_number', models.CharField(blank=True, max_length=10, verbose_name='№ УПД')),
                ('unload_date', models.DateField(blank=True, null=True, verbose_name='Дата выгрузки')),
            ],
            options={
                'verbose_name': 'ЗМК',
                'verbose_name_plural': 'ЗМК',
            },
        ),
        migrations.CreateModel(
            name='PlantObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField(verbose_name='Объект')),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='objects', to='plants.plant')),
            ],
            options={
                'verbose_name': 'Объект ЗМК',
                'verbose_name_plural': 'Объекты ЗМК',
            },
        ),
    ]