# cart/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import LocationViewSet, DepartmentViewSet, ProductViewSet, CartItemViewSet, CartViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'locations', LocationViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'products', ProductViewSet)
router.register(r'cart-items', CartItemViewSet)
router.register(r'carts', CartViewSet, basename='cart')
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]