from django.contrib import admin
from .models import OrderItem, Order

# Register your models here.


class OrderItemAdmin(admin.ModelAdmin):
    model = OrderItem
    list_display = ["product", "quantity",]

admin.site.register(OrderItem,OrderItemAdmin)


class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = [
        "id",
        "user",

    ]

admin.site.register(Order,OrderAdmin)