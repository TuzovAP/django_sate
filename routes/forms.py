from django import forms
from cities.models import City
from routes.models import Route
from trains.models import Train


class RouteForm(forms.Form):
    from_city = forms.ModelChoiceField(label='Откуда',  # ModelChoiceField - выпадающий список
                                       queryset=City.objects.all(),  # City.objects.all()) - отбор всех записей
                                       widget=forms.Select(  # Виджит для выбора
                                           attrs={'class': 'form-control js-example-basic-single'}  # красивое отображение для Bootstrap
                                       ))
    to_city = forms.ModelChoiceField(label='Куда',  # ModelChoiceField - выпадающий список
                                       queryset=City.objects.all(),  # City.objects.all()) - отбор всех записей
                                       widget=forms.Select(  # Виджит для выбора
                                           attrs={'class': 'form-control js-example-basic-single'}  # красивое отображение для Bootstrap
                                       ))
    # список городов через которые проложить маршрут
    cities =forms.ModelMultipleChoiceField(  # ModelMultipleChoiceField модель для выбора нескольких значений
        label='Через города', queryset=City.objects.all(),
        required=False,  # required - обязательное поле?
        widget=forms.SelectMultiple(attrs={'class': 'form-control js-example-basic-multiple'})
    )
    travelling_time = forms.IntegerField(label='Время в пути', widget=forms.NumberInput(attrs={  # виджет для отрисовки формы
        'class': 'form-control',  # красивое отображение для Bootstrap
        'placeholder': 'Время в пути'
    }))


class RouteModelForm(forms.ModelForm):
    name = forms.CharField(label='Название маршрута', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите название маршрута'
    }))
    from_city = forms.ModelChoiceField(queryset=City.objects.all(),  # City.objects.all()) - отбор всех записей
                                       widget=forms.HiddenInput())
    to_city = forms.ModelChoiceField(queryset=City.objects.all(),  # City.objects.all()) - отбор всех записей
                                       widget=forms.HiddenInput())
    # список городов через которые проложить маршрут
    trains = forms.ModelMultipleChoiceField(  # ModelMultipleChoiceField модель для выбора нескольких значений
        queryset=Train.objects.all(),
        required=False,  # required - обязательное поле?
        widget=forms.SelectMultiple(attrs={'class': 'form-control d-none'})
    )
    travel_times = forms.IntegerField(widget=forms.HiddenInput())


    class Meta:
        model = Route
        fields = '__all__'

