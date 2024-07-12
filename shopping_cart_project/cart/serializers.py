# cart/serializers.py

from rest_framework import serializers
from .models import Location, Department, Product, CartItem

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name', 'description']

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'description', 'is_taxable']

class ProductSerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only=True)
    department = DepartmentSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'image', 'barcode', 
                  'location', 'department', 'is_available', 'on_hand', 
                  'created_at', 'updated_at']

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    subtotal = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    tax = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'subtotal', 'tax', 'total_price', 
                  'created_at', 'updated_at']