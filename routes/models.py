from django.db import models

# Таблицы в БД
from cities.models import City
from trains.models import Train


class Route(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название маршрута')
    travel_time = models.PositiveSmallIntegerField(verbose_name='Общее время в пути')
    from_city = models.ForeignKey(City, on_delete=models.CASCADE,
                                  related_name='route_from_city_set',
                                  verbose_name='Откуда')
    to_city = models.ForeignKey('cities.City', on_delete=models.CASCADE,
                                  related_name='route_to_city_set',
                                  verbose_name='Куда')
    trains = models.ManyToManyField(Train, verbose_name='Список поездов')  # указания на несколько  записей в одной таблице

    def __str__(self):
        return f'Маршрут № {self.name} из города {self.from_city}'

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'
        ordering = ['travel_time']
