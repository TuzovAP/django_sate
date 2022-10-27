from django.contrib import admin
from trains.models import Train


class TrainAdmin(admin.ModelAdmin):
    class Meta():
        model = Train
    # список для отображения в админке на сайте
    list_display = ('name', 'from_city', 'to_city', 'travel_time')
    # что можно редактировать прямо в общей таблице в админке на сайте
    list_editable = ('travel_time',)

# регистрирую классы
admin.site.register(Train, TrainAdmin)