from .models import Form
from django.forms import ModelForm, TextInput, NumberInput

class FormForm(ModelForm):
    class Meta:
        model = Form

        fields = ['fio','job_title','url_progect','summ']

        widgets = {
            'fio': TextInput(attrs={
                'placeholder': 'ФИО'
            }),
            'job_title': TextInput(attrs={
                'placeholder': 'Работа'
            }),
            'url_progect': TextInput(attrs={
                'placeholder': 'Ссылка на проект'
            }),
            'summ': NumberInput(attrs={
                'placeholder': 'Стоимость',
                'step': '0.001',
                'min': '0',
                'class': 'money'
            })
        }