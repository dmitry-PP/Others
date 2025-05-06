from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import resolve_url
from django.urls import path, reverse_lazy, include
from . import views, api

urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('find', views.find, name="find"),
    path('goods', views.goods, name="goods"),
    path('category', views.category, name="category"),
    path('all-goods', views.all_goods, name="all_goods"),
    path('cart', views.basket_detail, name="cart"),
    path('order', views.order, name="order"),

    path('api/', include(api.router.urls)),

    path('cart-add/<int:product_id>', views.basket_add, name="basket_add"),
    path('cart-update', views.update_cart, name="update_cart"),

    path('login/', LoginView.as_view(template_name="products/forms/authorize.html",next_page="home"), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),

    path('admin-panel', views.admin_panel, name="admin_panel"),

    path('admin-panel/category', views.CategoryListView.as_view(), name="category_list"),
    path('admin-panel/category/new', views.CategoryCreateView.as_view(), name="category_new"),
    path('admin-panel/category/detail/<int:pk>', views.CategoryDetailView.as_view(), name="category_detail"),
    path('admin-panel/category/detail/edit/<int:pk>', views.CategoryUpdateView.as_view(), name="category_edit"),
    path('admin-panel/category/detail/delete/<int:pk>', views.CategoryDeleteView.as_view(), name="category_delete"),

    path('admin-panel/unit', views.UnitListView.as_view(), name="unit_list"),
    path('admin-panel/unit/new', views.UnitCreateView.as_view(), name="unit_new"),
    path('admin-panel/unit/detail/<int:pk>', views.UnitDetailView.as_view(), name="unit_detail"),
    path('admin-panel/unit/detail/edit/<int:pk>', views.UnitUpdateView.as_view(), name="unit_edit"),
    path('admin-panel/unit/detail/delete/<int:pk>', views.UnitDeleteView.as_view(), name="unit_delete"),

    path('admin-panel/status', views.StatusListView.as_view(), name="status_list"),
    path('admin-panel/status/new', views.StatusCreateView.as_view(), name="status_new"),
    path('admin-panel/status/detail/<int:pk>', views.StatusDetailView.as_view(), name="status_detail"),
    path('admin-panel/status/detail/edit/<int:pk>', views.StatusUpdateView.as_view(), name="status_edit"),
    path('admin-panel/status/detail/delete/<int:pk>', views.StatusDeleteView.as_view(), name="status_delete"),

    path('admin-panel/farmer', views.FarmerListView.as_view(), name="farmer_list"),
    path('admin-panel/farmer/new', views.FarmerCreateView.as_view(), name="farmer_new"),
    path('admin-panel/farmer/detail/<int:pk>', views.FarmerDetailView.as_view(), name="farmer_detail"),
    path('admin-panel/farmer/detail/edit/<int:pk>', views.FarmerUpdateView.as_view(), name="farmer_edit"),
    path('admin-panel/farmer/detail/delete/<int:pk>', views.FarmerDeleteView.as_view(), name="farmer_delete"),

    path('admin-panel/product', views.ProductListView.as_view(), name="product_list"),
    path('admin-panel/product/new', views.ProductCreateView.as_view(), name="product_new"),
    path('admin-panel/product/detail/<int:pk>', views.ProductDetailView.as_view(), name="product_detail"),
    path('admin-panel/product/detail/edit/<int:pk>', views.ProductUpdateView.as_view(), name="product_edit"),
    path('admin-panel/product/detail/delete/<int:pk>', views.ProductDeleteView.as_view(), name="product_delete"),

]
