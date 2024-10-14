from django import forms
from prompt_toolkit.validation import ValidationError

from catalog.models import Product, Version


class FormStylesMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.__class__.__name__ == 'CheckboxInput':
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'

class ProductForm(FormStylesMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'category', 'description','price', 'image',)

    def clean_name(self):
        words_prohibited = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево',\
                            'бесплатно', 'обман', 'полиция', 'радар']
        cleaned_data = self.cleaned_data['name']

        check_words = cleaned_data.split()
        for word in check_words:
            if word.lower() in words_prohibited:
                raise forms.ValidationError('Недопустимые слова в названии')
        return cleaned_data

class ProductModeratorForm(FormStylesMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('description', 'category', 'is_published',)




class VersionForm(FormStylesMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = ('name', 'product', 'number', 'is_current',)

    def clean_is_current(self):
        cleaned_data = self.cleaned_data['is_current']
        product =  self.cleaned_data['product']
        versions = Version.objects.filter(product=product, is_current=True)
        if len(versions) > 1 and cleaned_data:
            raise forms.ValidationError('Допустима только одна текущая версия')
        return cleaned_data







