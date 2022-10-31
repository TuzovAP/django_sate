from django.contrib import admin
from routes.models import Route

# таблицы которые буду видеть в алминке сайта
admin.site.register(Route)
