from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout

from . import models
from . import forms

# Create your views here.
from .basket import Basket
from .forms import CustomUserCreationForm, OrderForm
from .models import Product, Status, OrderItem


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


def admin_panel(request):
    return render(request, "products/admin/index.html", {"title": "Админ Панель"})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'products/forms/register.html', {'form': form})

@login_required(login_url="login")
def logout_view(request):
    logout(request)
    return redirect("login")


@login_required(login_url="login")
def basket_detail(request):
    basket = Basket(request)
    items = list(basket)
    total_price = basket.get_total_price()

    context = {
        'basket': basket,
        'cart_items': items,
        'total_price': total_price,
        'total_items': len(basket),
        'delivery_cost': 0 if total_price > 750 else 750,
        'title': "Корзина"
    }
    return render(request, "products/cart.html", context)


@login_required(login_url="login")
def order(request):
    basket = Basket(request)
    if len(basket) == 0:
        return redirect('cart')

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Создаем элементы заказа
            order_items = []
            for item in basket:
                product = item['product']
                order_item = OrderItem.objects.create(
                    product=product,
                    price=product.price,
                    quantity=item['count']
                )
                order_items.append(order_item)

            # Создаем заказ
            order = form.save(commit=False)
            order.user = request.user
            order.order_item = order_items[0]  # Первый элемент заказа
            order.status = Status.objects.get_or_create(name='В обработке')[0]
            order.total_sum = basket.get_total_price()
            order.save()

            # Привязываем остальные элементы заказа
            for item in order_items[1:]:
                order.order_item.add(item)

            # Очищаем корзину
            basket.clear()

            return redirect('home')
    else:
        form = OrderForm()

    context = {
        'form': form,
        'basket': basket,
        'delivery_cost': 0 if basket.get_total_price() > 750 else 750,
        'total_price': basket.get_total_price(),
    }
    return render(request, 'products/order.html', context)

@require_POST
@login_required
def update_cart(request):
    product_id = request.POST.get('product_id')
    action = request.POST.get('action')

    product = get_object_or_404(Product, id=product_id)
    basket = Basket(request)

    if action == 'increase':
        basket.add(product)
    elif action == 'decrease' and basket.get(product):
        if basket.get(product)["count"] > 1:
            basket.add(product, -1)
        else:
            basket.remove(product)
    elif action == 'remove':
        basket.remove(product)

    return JsonResponse({'success': True})

@require_POST
@login_required(login_url="login")
def basket_add(request, product_id):
    product = get_object_or_404(Product.objects.all(), pk=product_id)
    Basket(request).add(product)
    return redirect(reverse("product_detail", kwargs={"pk": product_id}))


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

class CategoryUpdateView(PermissionRequiredMixin, FormMixin, UpdateView):
    model = models.Category
    form_class = forms.CategoryForm
    success_url = reverse_lazy("category_list")
    action_name = "Изменить"
    permission_required = 'products.change_category'


class CategoryDeleteView(PermissionRequiredMixin, DeleteGeneralView):
    model = models.Category
    delete_title = "Категории"
    name_field_object = "name"
    prefix = "category"
    permission_required = 'products.delete_category'


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
    queryset = models.Product.objects.all()
    template_name = 'products/admin/product/detail.html'
    context_object_name = 'product'

    def get(self, request, *args, **kwargs):
        product = self.get_object()
        product_in_cart = False

        if request.user.is_authenticated and not (request.user.is_staff or request.user.is_superuser):
            basket = Basket(request)
            product_in_cart = (basket.get(product) is not None)

        context = {
            'product': product,
            'product_in_cart': product_in_cart,
        }
        return self.render_to_response(context)

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