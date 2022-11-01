from django import forms
from cities.models import City


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
