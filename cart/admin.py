from django.contrib import admin
from .models import Cart, CartItem


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'session_key', 'total_items', 'total_price', 'created_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['user__username', 'session_key']
    readonly_fields = ['created_at', 'updated_at']
    
    def total_items(self, obj):
        return obj.total_items
    total_items.short_description = 'Total Items'
    
    def total_price(self, obj):
        return f"Rs {obj.total_price}"
    total_price.short_description = 'Total Price'


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'cart', 'product', 'quantity', 'total_price', 'created_at']
    list_filter = ['created_at', 'updated_at', 'product__category']
    search_fields = ['product__name', 'cart__user__username']
    readonly_fields = ['created_at', 'updated_at']
    
    def total_price(self, obj):
        return f"Rs {obj.total_price}"
    total_price.short_description = 'Total Price'