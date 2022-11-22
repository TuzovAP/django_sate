from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView

from cities.models import City
from routes.forms import RouteForm, RouteModelForm
from routes.models import Route
from routes.utils import get_routes


# функция для прорисовки главной страницы приложения
from trains.models import Train


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

# функция для отработки запросов через форму поиска маршрута на сайте
def add_route(request):
    if request.method == 'POST':    # если форма заполнена через сайт
        context = {}
        data = request.POST
        if data:
            total_time = int(data['total_time'])
            from_city_id = int(data['from_city'])
            to_city_id = int(data['to_city'])
            trains = data['trains'].split(',')
            trains_lst = [int(t) for t in trains if t.isdigit()]
            qs = Train.objects.filter(id__in=trains_lst).select_related(
                'from_city', 'to_city')
            cities = City.objects.filter(id__in=trains_lst).select_related(
                'from_city_id', 'to_city_id')
            form = RouteModelForm(
                initial={'from_city': cities[from_city_id],
                         'to_city': cities[to_city_id],
                         'travel_times': total_time,
                         'trains': qs,
                         }
            )
            context['form'] = form
        return render(request, 'routes/create.html', context)
    else:                           # если пользователь самойстоятельно указал адрес через браузер
        messages.error(request, 'Не возможно сохранить не существующий маршрут')
        return redirect('/')  # отправляю на основную страницу с формой

# функция для сохранения маршрута
# в файле travel.urls прописывается адрес/имя этой функции: path('save_route/', save_route, name='save_route'),
def save_route(request):
    if request.method == 'POST':    # если форма заполнена через сайт
        form = RouteModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Маршрут сохранен')
            return redirect('/')  # отправляю на основную страницу с формой
        return render(request, 'routes/create.html', {'form': form})
    else:                           # если пользователь самойстоятельно указал адрес через браузер
        messages.error(request, 'Не возможно сохранить не существующий маршрут')
        return redirect('/')  # отправляю на основную страницу с формой


class RouteListView(ListView):
    paginate_by = 5  # count record on page
    model = Route
    template_name = 'routes/list.html'


# этот класс нужно прописать в файле travel.urls
class RouteDetailView(DetailView):
    queryset = Route.objects.all()
    template_name = 'routes/detail.html'



class RouteDeleteView(LoginRequiredMixin, DeleteView):
    model = Route  # таблица городов в БД
    template_name = 'trains/delete.html'  # шаблон для отрисовки страницы с подтверждением
    success_url = reverse_lazy('home')  # в случае успеха переходим на home, но нужно использовать ленивый реверс
    #  функуия для удаления без подтверждения. Не работает, видимо из-за новой версии джанго
    def get(self, request, *args, **kwargs):
        messages.success(request, 'Маршрут успешно удален')
        return self.post(request, *args, **kwargs)


