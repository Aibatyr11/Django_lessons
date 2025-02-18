from dataclasses import fields
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm, modelform_factory, DecimalField
from django.forms.widgets import Select

from bboard.models import Bb, Rubric

from django.core import validators


#1
# BbForm = modelform_factory(
#     Bb,
#     fields=('title', 'content', 'price', 'rubric'),
#     labels={'title': 'Название товара'},
#     help_texts={'rubric':'Не забудьте выбрать рубрику'},
#     field_classes={'price': DecimalField},
#     widgets={'rubric': Select(attrs={'size': 8})}
# )


#2
# class BbForm(ModelForm):
#     class Meta:
#         model = Bb
#         fields = ('title', 'content', 'price', 'rubric')
#         labels={'title': 'Название товара'}
#         help_texts={'rubric':'Не забудьте выбрать рубрику'}
#         field_classes={'price': DecimalField}
#         widgets={'rubric': Select(attrs={'size': 8})}


#3
class BbForm(ModelForm):
    title = forms.CharField(label="Название товара",
                            validators=[validators.RegexValidator(regex='^.{4,}$')],
                            error_messages={'invalid': 'Сдишком короткое название'})
    content = forms.CharField(label="Описание", widget=forms.Textarea())
    price = forms.DecimalField(label='Цена',  decimal_places=2)
    rubric = forms.ModelChoiceField(queryset=Rubric.objects.all(),
                                    label='Рубрика', help_text='Не забудьте выбрать рубрику',
                                    widget = forms.widgets.Select(attrs={'size':8}))


    def clean_title(self):
        val = self.cleaned_data['title']
        if val == 'Прошлогодний снег':
            raise ValidationError('К продаже не допуск')
        return val

    def clean(self):
        super().clean()
        errors = {}
        if not self.cleaned_data['content']:
            errors['content'] = ValidationError(
                'кажите описание товара'
            )

        if not self.cleaned_data['price'] < 0:
            errors['price'] = ValidationError(
                'price>0'
            )
        if errors:
            raise ValidationError(errors)


    class Meta:
        model = Bb
        fields = ('title', 'content', 'price', 'rubric')

    class RegisterUserForm(forms.ModelForm):
        password1 = forms.CharField(label="password")
        password2 = forms.CharField(label="password (повторно)") #подтвердить

        class Meta:
            model = User
            fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')
