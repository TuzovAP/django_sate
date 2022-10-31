from django import forms

from cities.models import City
from trains.models import Train


class TrainForm(forms.ModelForm):
    name = forms.CharField(label='Номер поезда', widget=forms.TextInput(attrs={  # виджет для отрисовки формы
        'class': 'form-control',  # красивое отображение для Bootstrap
        'placeholder': 'Введите номер поезда'
    }))

    travel_time = forms.IntegerField(label='Время в пути', widget=forms.NumberInput(attrs={  # виджет для отрисовки формы
        'class': 'form-control',  # красивое отображение для Bootstrap
        'placeholder': 'Время в пути'
    }))


    from_city = forms.ModelChoiceField(label='Откуда',  # ModelChoiceField - выпадающий список
                                       queryset=City.objects.all(),  # City.objects.all()) - отбор всех записей
                                       widget=forms.Select(  # Виджит для выбора
                                           attrs={'class': 'form-control'}  # красивое отображение для Bootstrap
                                       ))

    to_city = forms.ModelChoiceField(label='Куда',  # ModelChoiceField - выпадающий список
                                       queryset=City.objects.all(),  # City.objects.all()) - отбор всех записей
                                       widget=forms.Select(  # Виджит для выбора
                                           attrs={'class': 'form-control'}  # красивое отображение для Bootstrap
                                       ))




    class Meta:
        model = Train  # к какой модели будет привязана форма
        fields = ('__all__', )  # все поля которые есть в таблице будут отображены
        # fields = ('name', )  # поля которые будут отображены
