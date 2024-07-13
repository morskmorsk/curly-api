# cart/admin.py

from django.contrib import admin
from .models import Product, CartItem, Location, Department, Cart, CartItem, Order, OrderItem

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'is_taxable')
    list_filter = ('is_taxable',)
    search_fields = ('name', 'description')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'location', 'department', 'is_available', 'on_hand', 'created_at', 'updated_at')
    list_filter = ('is_available', 'location', 'department', 'department__is_taxable')
    search_fields = ('name', 'description', 'barcode')

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'subtotal', 'tax', 'total_price', 'created_at', 'updated_at')
    list_filter = ('product__department', 'product__location', 'product__department__is_taxable')

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'total', 'created_at', 'updated_at')
    list_filter = ('user',)
    search_fields = ('user',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'total', 'created_at', 'updated_at')
    list_filter = ('user',)
    search_fields = ('user',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity')
    list_filter = ('product__department', 'product__location', 'product__department__is_taxable')
    search_fields = ('product', 'quantity', 'subtotal', 'tax', 'total_price')
