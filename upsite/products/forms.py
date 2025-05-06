from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone

from .models import Category, UnitOfMeasurement, Product, Farmer, Status, Order


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = "__all__"

class UnitOfMeasurementForm(forms.ModelForm):
    class Meta:
        model = UnitOfMeasurement
        fields = "__all__"


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class FarmerForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = "__all__"

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = "__all__"


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["email", "first_name", "last_name"] + list(UserCreationForm.Meta.fields)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['delivery_date', 'address', "fio", "comment"]
        widgets = {
            'delivery_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'address': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_delivery_date(self):
        delivery_date = self.cleaned_data['delivery_date']
        if delivery_date < timezone.now():
            raise forms.ValidationError("Дата доставки не может быть в прошлом")
        return delivery_date