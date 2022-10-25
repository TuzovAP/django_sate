from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from cities.forms import HtmlForm, CityForm
from cities.models import City


# функция для прорисовки страницы home
def home(request, pk=None):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
    # if pk:
    #     # city = City.objects.filter(id=pk).first()
    #     city = get_object_or_404(City, id=pk)
    #     content = {'object': city}
    #     return render(request, 'cities/detail.html', content)
    form = CityForm()
    qs = City.objects.all()
    lst = Paginator(qs, 2)
    page_num = request.GET.get('page')
    page_obj = lst.get_page(page_num)
    content = {'page_obj': page_obj, 'form': form}
    return render(request, 'cities/home.html', content)


class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'


class CityCreateView(CreateView):
    model = City  # таблица городов в БД
    form_class = CityForm  # модель формы через django
    template_name = 'cities/create.html'
    success_url = reverse_lazy('cities:home')  # в случае успеха переходим на cities:home, но нужно испольховать ленивый реверс


class CityUpdateView(UpdateView):
    model = City  # таблица городов в БД
    form_class = CityForm  # модель формы через django
    template_name = 'cities/update.html'
    success_url = reverse_lazy('cities:home')  # в случае успеха переходим на cities:home, но нужно использовать ленивый реверс

class CityDeleteView(DeleteView):
    model = City  # таблица городов в БД
    template_name = 'cities/delete.html'  # шаблон для отрисовки страницы с подтверждением
    success_url = reverse_lazy('cities:home')  # в случае успеха переходим на cities:home, но нужно использовать ленивый реверс
    #  функуия для удаления без подтверждения. Не работает, видимо из-за новой версии джанго
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class CityListView(ListView):
    paginate_by = 2
    model = City
    template_name = 'cities/home.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        form = CityForm()
        # Add in a QuerySet of all the books
        context['form'] = form
        return context
