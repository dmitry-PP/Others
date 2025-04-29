from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('find', views.find, name="find"),
    path('goods', views.goods, name="goods"),
    path('category', views.category, name="category"),
    path('all-goods', views.all_goods, name="all_goods"),
    path('cart', views.cart, name="cart"),
]