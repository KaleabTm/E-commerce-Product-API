from django.contrib import admin
from .models import CartItem, Cart

# Register your models here.


class CartItemAdmin(admin.ModelAdmin):
    model = CartItem
    list_display = ["product", "quantity",]

admin.site.register(CartItem,CartItemAdmin)


class CartAdmin(admin.ModelAdmin):
    model = Cart
    list_display = [
        "id",
        "user",

    ]