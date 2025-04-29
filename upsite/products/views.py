from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "products/index.html")

def about(request):
    return render(request, "products/about.html")

def contact(request):
    return render(request, "products/contact.html")

def find(request):
    return render(request, "products/find.html")

def goods(request):
    return render(request, "products/goods.html")

def category(request):
    return render(request, "products/category.html")

def all_goods(request):
    return render(request, "products/all_goods.html")

def cart(request):
    return render(request, "products/cart.html")

