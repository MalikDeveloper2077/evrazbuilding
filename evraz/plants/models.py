from django.db import models

from plants.services.plants import import_plants_from_table


PLANT_STATUSES = [
    ('Выгрузился', 'Выгрузился'),
    ('Возврат', 'Возврат')
]


class Plant(models.Model):
    date = models.DateField('Дата погрузки')
    weight = models.FloatField('Вес (тн)')
    status = models.CharField('Статус', max_length=15, choices=PLANT_STATUSES, blank=True)
    upd_number = models.CharField('№ УПД', max_length=10, blank=True)
    unload_date = models.DateField('Дата выгрузки', null=True, blank=True)

    class Meta:
        verbose_name = 'ЗМК'
        verbose_name_plural = 'ЗМК'

    def __str__(self):
        return f'{str(self.date)} {str(self.weight)}'


class PlantObject(models.Model):
    plant = models.ForeignKey(Plant, models.CASCADE, related_name='plant_objects')
    value = models.FloatField('Объект')

    class Meta:
        verbose_name = 'Объект ЗМК'
        verbose_name_plural = 'Объекты ЗМК'

    def __str__(self):
        return str(self.value) + ' ' + str(self.plant.id)


class ImportPlantsToggle(models.Model):
    to_import = models.BooleanField('Для запуска импорта просто сохраните объект', default=True)

    class Meta:
        verbose_name = 'Запуск импорта'
        verbose_name_plural = 'Запуск импорта'

    def save(self, *args, **kwargs):
        if not ImportPlantsToggle.objects.exists():
            super().save(*args, **kwargs)

        Plant.objects.all().delete()
        PlantObject.objects.all().delete()

        plants, plants_objects = import_plants_from_table()
        Plant.objects.bulk_create([Plant(**plant) for plant in plants])
        PlantObject.objects.bulk_create([
            PlantObject(value=plant_val, plant_id=plant_id)
            for plant_obj, plant_id in zip(plants_objects, Plant.objects.values_list('id', flat=True))
            for plant_val in plant_obj
        ])

    def __str__(self):
        return 'Запуск'
