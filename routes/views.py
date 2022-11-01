from django.contrib import messages
from django.shortcuts import render
from routes.forms import RouteForm
from routes.utils import get_routes


# функция для прорисовки главной страницы приложения
def home(request):
    form = RouteForm()
    return render(request, 'routes/home.html', {'form': form})

# функция для отработки запросов через форму поиска маршрута на сайте
def find_routes(request):
    if request.method == 'POST':    # если форма заполнена через сайт
        form = RouteForm(request.POST)
        if form.is_valid():
            try:  # функция может отрабатывать с ошибками
                context = get_routes(request, form)
            except ValueError as ex:
                messages.error(request, ex)
                return render(request, 'routes/home.html', {'form': form})
            return render(request, 'routes/home.html', context)
        return render(request, 'routes/home.html', {'form': form})
    else:                           # если пользователь самойстоятельно указал адрес через браузер
        form = RouteForm()
        messages.error(request, 'Нет данных для поиска')
        return render(request, 'routes/home.html', {'form': form})  # отправляю на основную страницу с формой
