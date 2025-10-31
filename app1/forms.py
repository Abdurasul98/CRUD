import re
from django import forms
from django.core.exceptions import ValidationError
from .models import *


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            "category_name": forms.TextInput(attrs={'class': 'form-control'}),
            }

    def clean_category(self):
        category_name = self.cleaned_data['category_name']

        if re.match(r'\d',category_name):
            raise ValidationError("Son qoshish mumkin emas boshiga")
        return category_name



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        widgets = {
            "product_name": forms.TextInput(attrs={'class': 'form-control'}),
            "unit_price": forms.NumberInput(attrs={'class': 'form-control'}),
            }

    def clean_unit_price(self):
        unit_price = self.cleaned_data['unit_price']

        if unit_price < 0:
            raise ValidationError('Faqat musbat sonlar')
        return unit_price



class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            "last_name": forms.TextInput(attrs={'class': 'form-control'}),
            "first_name": forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']

        if re.match(r'\d',first_name):
            raise ValidationError("Son qoshish mumkin emas boshiga")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']

        if re.match(r'\d',last_name):
            raise ValidationError("Son qoshish mumkin emas boshiga")
        return last_name

    def clean_title(self):
        title = self.cleaned_data['title']

        if re.match(r'\d',title):
            raise ValidationError('Son qoshish mumkin emas boshiga')
        return title



class OrderDetailForm(forms.ModelForm):
    class Meta:
        model = OrderDetail
        fields = '__all__'

        widgets = {
            "quantity": forms.NumberInput(attrs={'class': 'form-control'}),
            "unit_price": forms.NumberInput(attrs={'class': 'form-control'})
        }

    def clean_unit_price(self):
        unit_price = self.cleaned_data['unit_price']

        if unit_price < 0:
            raise ValidationError('Faqat musbat sonlar')
        return unit_price

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity < 0:
            raise ValidationError('Faqat musbat sonlar')
        return quantity



class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

        widgets = {
            "order_date": forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            "required_date": forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            "shipped_date": forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
