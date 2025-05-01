from django import forms
from .models import Category, UnitOfMeasurement, Product, Farmer, Status


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