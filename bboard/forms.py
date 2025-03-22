from cProfile import label
#from collections.abc import generator
from dataclasses import fields
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm, modelform_factory, DecimalField, modelformset_factory, BaseModelFormSet
from django.forms.widgets import Select

from bboard.models import Bb, Rubric
from captcha.fields import CaptchaField
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


    captcha = CaptchaField(
        label='Введите текст',
        error_messages={'invalid': 'Неправильный текст'},
        # generator='captcha.helpers.random_char_challenge',
        # generator='captcha.helpers.math_challenge'
        #generator='captcha.helpers.word_challenge'
    )

    my_field_hw_31 = forms.CharField(
        label='Введите текст',
    )

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

        if self.cleaned_data['price'] < 0:
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





class RubricBaseFormSet(BaseModelFormSet):
    def clean(self):
        super().clean()
        names = [form.cleaned_data['name'] for form in self.forms
                 if 'name' in form.cleaned_data]

        if ('Недвижимость' not in names) or ('Транспорт' not in names) or ('Мебель' not in names):
            raise ValidationError(
                'Добавьте рубрику Недвижимость, Транспорт, Мебель'
            )




class MyForm(forms.Form):
    name = forms.CharField(max_length=100)


class SearchForm(forms.Form):
    keyword = forms.CharField(max_length=20, label="Искомое слово")
    rubric = forms.ModelChoiceField(queryset=Rubric.objects.all(),
                                    label='Rubric')



from .models import My_hw_BBCODE
#hw32

class hw_BBCODE_FORM(forms.ModelForm):
    class Meta:
        model = My_hw_BBCODE
        fields = ['content']




