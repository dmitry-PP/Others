from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Farmer)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(UnitOfMeasurement)
admin.site.register(Status)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(Review)