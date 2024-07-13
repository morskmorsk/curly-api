# cart/tests.py

from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Product, Department, Location, Cart, Order

class ShoppingCartAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.admin = User.objects.create_superuser(username='admin', password='admin123')
        
        self.department = Department.objects.create(name='Electronics', is_taxable=True)
        self.location = Location.objects.create(name='Warehouse A')
        
        self.product = Product.objects.create(
            name='Test Product',
            price=99.99,
            department=self.department,
            location=self.location,
            on_hand=10
        )

    def test_product_list(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('results', response.data)
        self.assertGreater(len(response.data['results']), 0)

    def test_add_to_cart(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post('/api/carts/add_item/', {'product_id': self.product.id, 'quantity': 2})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        cart = Cart.objects.get(user=self.user)
        self.assertEqual(cart.items.count(), 1)
        self.assertEqual(cart.items.first().quantity, 2)

    def test_checkout(self):
        self.client.force_authenticate(user=self.user)
        cart = Cart.objects.create(user=self.user)
        cart.items.create(product=self.product, quantity=1)
        response = self.client.post('/api/orders/checkout/')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.filter(user=self.user).count(), 1)

    def test_admin_create_product(self):
        self.client.force_authenticate(user=self.admin)
        data = {
            'name': 'New Product',
            'price': 49.99,
            'department': self.department.id,
            'location': self.location.id,
            'on_hand': 5
        }
        response = self.client.post('/api/products/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)

    def test_user_create_product_forbidden(self):
        self.client.force_authenticate(user=self.user)
        data = {
            'name': 'New Product',
            'price': 49.99,
            'department': self.department.id,
            'location': self.location.id,
            'on_hand': 5
        }
        response = self.client.post('/api/products/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)