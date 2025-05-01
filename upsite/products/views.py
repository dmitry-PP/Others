from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin

from . import models
from . import forms

# Create your views here.
def index(request):
    return render(request, "products/index.html", {"title": "Главная"})

def about(request):
    return render(request, "products/about.html", {"title": "О нас"})

def contact(request):
    return render(request, "products/contact.html", {"title": "Контакты"})

def find(request):
    return render(request, "products/find.html", {"title": "Как нас найти"})

def goods(request):
    return render(request, "products/goods.html", {"title": "Товары"})

def category(request):
    return render(request, "products/category.html", {"title": "Категории"})

def all_goods(request):
    return render(request, "products/all_goods.html", {"title": "Все товары"})

def cart(request):
    return render(request, "products/cart.html", {"title": "Корзина"})

def admin_panel(request):
    return render(request, "products/admin/index.html", {"title": "Админ Панель"})

class DeleteGeneralView(DeleteView):
    template_name = 'products/admin/delete.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.success_url = reverse_lazy(f"{self.prefix}_list")
        self.back_url = f"{self.prefix}_detail"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = context["object"]

        context["delete_title"] = getattr(self, "delete_title", "")
        context["name"] = getattr(obj, self.name_field_object)
        context["back_url"] = reverse(self.back_url, kwargs={
            self.pk_url_kwarg: getattr(obj, self.pk_url_kwarg)
        })
        return context

class FormMixin:
    template_name = 'products/admin/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["action_name"] = getattr(self, "action_name", "")
        return context

# ___________________________________________
class CategoryListView(ListView):
    model = models.Category
    template_name = 'products/admin/category/list.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = models.Category
    template_name = 'products/admin/category/detail.html'
    context_object_name = 'category'

class CategoryCreateView(FormMixin, CreateView):
    model = models.Category
    form_class = forms.CategoryForm
    success_url = reverse_lazy("category_list")
    action_name = "Добавить"

class CategoryUpdateView(FormMixin, UpdateView):
    model = models.Category
    form_class = forms.CategoryForm
    success_url = reverse_lazy("category_list")
    action_name = "Изменить"

class CategoryDeleteView(DeleteGeneralView):
    model = models.Category
    delete_title = "Категории"
    name_field_object = "name"
    prefix = "category"

# ___________________________________________


class UnitListView(ListView):
    model = models.UnitOfMeasurement
    template_name = 'products/admin/unit/list.html'
    context_object_name = 'units'

class UnitDetailView(DetailView):
    model = models.UnitOfMeasurement
    template_name = 'products/admin/unit/detail.html'
    context_object_name = 'unit'

class UnitCreateView(FormMixin, CreateView):
    model = models.UnitOfMeasurement
    form_class = forms.UnitOfMeasurementForm
    success_url = reverse_lazy("unit_list")
    action_name = "Добавить"

class UnitUpdateView(FormMixin, UpdateView):
    model = models.UnitOfMeasurement
    form_class = forms.UnitOfMeasurementForm
    success_url = reverse_lazy("unit_list")
    action_name = "Изменить"

class UnitDeleteView(DeleteGeneralView):
    model = models.UnitOfMeasurement
    delete_title = "Единицы измерения"
    name_field_object = "name"
    prefix = "unit"
# ___________________________________________


class StatusListView(ListView):
    model = models.Status
    template_name = 'products/admin/status/list.html'
    context_object_name = 'statuses'

class StatusDetailView(DetailView):
    model = models.Status
    template_name = 'products/admin/status/detail.html'
    context_object_name = 'status'

class StatusCreateView(FormMixin, CreateView):
    model = models.Status
    form_class = forms.StatusForm
    success_url = reverse_lazy("status_list")
    action_name = "Добавить"

class StatusUpdateView(FormMixin, UpdateView):
    model = models.Status
    form_class = forms.StatusForm
    success_url = reverse_lazy("status_list")
    action_name = "Изменить"

class StatusDeleteView(DeleteGeneralView):
    model = models.Status
    delete_title = "Статуса заказа"
    name_field_object = "name"
    prefix = "status"

# ___________________________________________


class FarmerListView(ListView):
    model = models.Farmer
    template_name = 'products/admin/farmer/list.html'
    context_object_name = 'farmers'

class FarmerDetailView(DetailView):
    model = models.Farmer
    template_name = 'products/admin/farmer/detail.html'
    context_object_name = 'farmer'

class FarmerCreateView(FormMixin, CreateView):
    model = models.Farmer
    form_class = forms.FarmerForm
    success_url = reverse_lazy("farmer_list")
    action_name = "Добавить"

class FarmerUpdateView(FormMixin, UpdateView):
    model = models.Farmer
    form_class = forms.FarmerForm
    success_url = reverse_lazy("farmer_list")
    action_name = "Изменить"

class FarmerDeleteView(DeleteGeneralView):
    model = models.Farmer
    delete_title = "Фермера"
    name_field_object = "name"
    prefix = "farmer"

# ___________________________________________


class ProductListView(ListView):
    model = models.Product
    template_name = 'products/admin/product/list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = models.Product
    template_name = 'products/admin/product/detail.html'
    context_object_name = 'product'

class ProductCreateView(FormMixin, CreateView):
    model = models.Product
    form_class = forms.ProductForm
    success_url = reverse_lazy("product_list")
    action_name = "Добавить"

class ProductUpdateView(FormMixin, UpdateView):
    model = models.Product
    form_class = forms.ProductForm
    success_url = reverse_lazy("product_list")
    action_name = "Изменить"

class ProductDeleteView(DeleteGeneralView):
    model = models.Product
    delete_title = "Продукта"
    name_field_object = "name"
    prefix = "product"