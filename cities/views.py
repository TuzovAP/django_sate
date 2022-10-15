from django.shortcuts import render

from cities.models import City


def home(request):
    qs = City.objects.all()
    content = {'objects_list': qs}
    return render(request, 'cities/home.html', content)
