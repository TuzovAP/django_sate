from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from cities.forms import HtmlForm, CityForm
from cities.models import City


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
    content = {'objects_list': qs, 'form': form}
    return render(request, 'cities/home.html', content)


class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'
