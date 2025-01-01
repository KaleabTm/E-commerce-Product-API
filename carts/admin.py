from django.contrib import admin
from .models import CartItem

# Register your models here.


class CartItemAdmin(admin.TabularInline):
    model = CartItem
    list_fields = ["product", "quantity", "discounted_price", "item_total_price"]
