from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.routers import SimpleRouter

from .models import (
    Farmer, Category, UnitOfMeasurement, Product,
    Status, OrderItem, Order, Cart, Review
)
from .serializers import (
    FarmerSerializer, CategorySerializer, UnitOfMeasurementSerializer,
    ProductSerializer, StatusSerializer, OrderItemSerializer,
    OrderSerializer, CartSerializer, ReviewSerializer
)

from rest_framework import permissions

class CustomPermissions(permissions.DjangoModelPermissions):
    perms_map = {
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s']
    }

class PermissionMixin:
    permission_classes = [CustomPermissions]
    def get_permissions(self):
        if self.action in {'create', 'update', 'partial_update', 'destroy'}:
            return [IsAdminUser()]
        return [IsAuthenticated()]

class FarmerViewSet(PermissionMixin, viewsets.ModelViewSet):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer

class CategoryViewSet(PermissionMixin, viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class UnitOfMeasurementViewSet(PermissionMixin, viewsets.ModelViewSet):
    queryset = UnitOfMeasurement.objects.all()
    serializer_class = UnitOfMeasurementSerializer

class ProductViewSet(PermissionMixin, viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class StatusViewSet(PermissionMixin, viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class OrderItemViewSet(PermissionMixin, viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class OrderViewSet(PermissionMixin, viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class CartViewSet(PermissionMixin, viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class ReviewViewSet(PermissionMixin, viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


router = SimpleRouter()

# Регистрируем ViewSets в роутере
router.register(r'farmers', FarmerViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'units', UnitOfMeasurementViewSet)
router.register(r'products', ProductViewSet)
router.register(r'statuses', StatusViewSet)
router.register(r'order-items', OrderItemViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'carts', CartViewSet)
router.register(r'reviews', ReviewViewSet)


