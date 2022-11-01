from django.contrib import messages
from django.shortcuts import render
from routes.forms import RouteForm


# функция для прорисовки главной страницы приложения
def home(request):
    form = RouteForm()
    return render(request, 'routes/home.html', {'form': form})

# функция для отработки запросов через форму поиска маршрута на сайте
def find_routes(request):
    if request.method == 'POST':    # если форма заполнена через сайт
        form = RouteForm(request.POST)
        a = 1
        return render(request, 'routes/home.html', {'form': form})
    else:                           # если пользователь самойстоятельно указал адрес через браузер
        form = RouteForm()
        messages.error(request, 'Нет данных для поиска')
        return render(request, 'routes/home.html', {'form': form})  # отправляю на основную страницу с формой
