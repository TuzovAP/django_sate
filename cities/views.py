from django.shortcuts import render, get_object_or_404

from cities.models import City


def home(request, pk=None):
    if pk:
        # city = City.objects.filter(id=pk).first()
        city = get_object_or_404(City, id=pk)
        content = {'object': city}
        return render(request, 'cities/detail.html', content)
    qs = City.objects.all()
    content = {'objects_list': qs}
    return render(request, 'cities/home.html', content)
