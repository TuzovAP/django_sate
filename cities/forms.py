from django import forms

from cities.models import City


class HtmlForm(forms.Form):
    name = forms.CharField(label='Город')


class CityForm(forms.ModelForm):
    name = forms.CharField(label='Город', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите название города'
    }))
    class Meta:
        model = City  # к какой модели будет привязана форма
        fields = ('name', )  # поля которые будут отображены