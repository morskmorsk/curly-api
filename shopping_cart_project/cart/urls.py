from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from .views import ProductViewSet, CartViewSet, OrderViewSet, LocationViewSet, DepartmentViewSet, register_user, CustomTokenObtainPairView

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'carts', CartViewSet, basename='cart')
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', register_user, name='register'),
    path('carts/remove_item/', CartViewSet.as_view({'delete': 'remove_item'}), name='cart-remove-item'),
]
