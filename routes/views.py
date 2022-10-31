from django.shortcuts import render
from routes.forms import RouteForm


# функция для прорисовки главной страницы приложения
def home(request):
    form = RouteForm()
    return render(request, 'routes/home.html', {'form': form})