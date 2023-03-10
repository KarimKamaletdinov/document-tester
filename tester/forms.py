from django import forms
from django.core.validators import FileExtensionValidator


class SettingsForm(forms.Form):
    margin_left = forms.IntegerField(label='Левое поле, мм', initial=20, min_value=0)
    margin_top = forms.IntegerField(label='Верхнее поле, мм', initial=20, min_value=0)
    margin_bottom = forms.IntegerField(label='Нижнее поле, мм', initial=20, min_value=0)
    margin_right = forms.IntegerField(label='Правое поле, мм', initial=10, min_value=0)
    font_name = forms.CharField(label='Название шрифта', initial='Times New Roman')


class DocumentForm(forms.Form):
    document = forms.FileField(label='Загрузите документ .docx')
