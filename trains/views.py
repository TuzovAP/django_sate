from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

# from trains.forms import HtmlForm, TrainForm
from trains.models import Train




# функция для прорисовки страницы home
def home(request, pk=None):
    qs = Train.objects.all()
    lst = Paginator(qs, 5)  # count record on page
    page_num = request.GET.get('page')
    page_obj = lst.get_page(page_num)
    content = {'page_obj': page_obj,}
    return render(request, 'trains/home.html', content)

class TrainListView(ListView):
    paginate_by = 5  # count record on page
    model = Train
    template_name = 'trains/home.html'


class TrainDetailView(DetailView):
    queryset = Train.objects.all()
    template_name = 'trains/detail.html'
#
#
# class TrainCreateView(SuccessMessageMixin, CreateView):
#     model = Train  # таблица городов в БД
#     form_class = TrainForm  # модель формы через django
#     template_name = 'trains/create.html'
#     success_url = reverse_lazy('trains:home')  # в случае успеха переходим на trains:home, но нужно испольховать ленивый реверс
#     success_message = "Город успешно создан"
#
#
# class TrainUpdateView(SuccessMessageMixin, UpdateView):
#     model = Train  # таблица городов в БД
#     form_class = TrainForm  # модель формы через django
#     template_name = 'trains/update.html'
#     success_url = reverse_lazy('trains:home')  # в случае успеха переходим на trains:home, но нужно использовать ленивый реверс
#     success_message = "Город успешно отредактирован"
#
# class TrainDeleteView(DeleteView):
#     model = Train  # таблица городов в БД
#     template_name = 'trains/delete.html'  # шаблон для отрисовки страницы с подтверждением
#     success_url = reverse_lazy('trains:home')  # в случае успеха переходим на trains:home, но нужно использовать ленивый реверс
#     #  функуия для удаления без подтверждения. Не работает, видимо из-за новой версии джанго
#     def get(self, request, *args, **kwargs):
#         messages.success(request, 'Город успешно удален')
#         return self.post(request, *args, **kwargs)



